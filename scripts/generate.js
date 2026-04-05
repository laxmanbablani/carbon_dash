const fs = require('fs-extra');
const path = require('path');
const config = require('./config.json');

const DEST_COMPONENTS_DIR = path.resolve(__dirname, '../src/lib/components');
const DEST_FRAGMENTS_DIR = path.resolve(__dirname, '../src/lib/fragments');
const DEST_TESTS_DIR = path.resolve(__dirname, '../tests');
const CARBON_SRC_DIR = path.resolve(__dirname, '../_ref/carbon-design-system/packages/react/src/components');

function extractPropsFromSource(name) {
  // Common skeleton patterns
  let baseName = name;
  let isSkeleton = false;
  if (name.endsWith('Skeleton')) {
    baseName = name.replace('Skeleton', '');
    isSkeleton = true;
  }

  const componentDir = path.join(CARBON_SRC_DIR, baseName);
  if (!fs.existsSync(componentDir)) return {};

  const files = fs.readdirSync(componentDir);
  const targetFile = isSkeleton 
    ? files.find(f => f.toLowerCase().includes('skeleton') && (f.endsWith('.tsx') || f.endsWith('.js')))
    : files.find(f => (f === `${baseName}.tsx` || f === `${baseName}.js` || f === 'index.tsx' || f === 'index.js'));

  if (!targetFile) return {};

  const source = fs.readFileSync(path.join(componentDir, targetFile), 'utf8');
  const props = {};

  // Regex to find props in function signature: function Component({ prop1, prop2 = default })
  // This is a simplified regex but should capture most destructured props in Carbon
  const funcPattern = new RegExp(`(?:function|const)\\s+${name}\\s*(?:=\\s*)?\\(\\s*{([^}]*)}\\s*\\)`, 's');
  const match = source.match(funcPattern);
  
  if (match && match[1]) {
    const propLines = match[1].split(',');
    propLines.forEach(line => {
        const propMatch = line.trim().match(/^([a-zA-Z0-9_]+)(?:\s*[:=]\s*.*)?$/);
        if (propMatch && propMatch[1] && propMatch[1] !== 'rest' && propMatch[1] !== 'other') {
            props[propMatch[1]] = 'PropTypes.any';
        }
    });
  }

  // Also look for propTypes definition in source if available (more reliable than runtime if runtime is stripped)
  const propTypesPattern = new RegExp(`${name}\\.propTypes\\s*=\\s*{([^}]*)}`, 's');
  const ptMatch = source.match(propTypesPattern);
  if (ptMatch && ptMatch[1]) {
    const ptLines = ptMatch[1].split('\n');
    ptLines.forEach(line => {
      const lineMatch = line.trim().match(/^([a-zA-Z0-9_]+)\s*:/);
      if (lineMatch && lineMatch[1]) {
        props[lineMatch[1]] = 'PropTypes.any';
      }
    });
  }

  return props;
}

async function generateComponent(name, CarbonComponent, compConfig) {
  if (!CarbonComponent) {
    console.error(`Error: Component ${name} not found. Skipping and cleaning up.`);
    
    // Cleanup orphaned files if they exist to prevent build errors or stale components
    const fragmentPath = path.join(DEST_FRAGMENTS_DIR, `${name}.react.js`);
    const componentPath = path.join(DEST_COMPONENTS_DIR, `${name}.react.js`);
    const pythonPath = path.join(path.resolve(__dirname, '../carbon_dash'), `${name}.py`);
    
    [fragmentPath, componentPath, pythonPath].forEach(p => {
        if (fs.existsSync(p)) {
            fs.unlinkSync(p);
            console.log(`  Cleaned up orphaned file: ${p}`);
        }
    });
    return;
  }

  console.log(`Generating wrappers for ${name}...`);

  const hasAILabel = compConfig.propTransforms && compConfig.propTransforms.ai_label === 'AILabel';

  // Merge Carbon's propTypes with our custom injected props
  const sourceProps = extractPropsFromSource(name);
  const carbonPropTypes = { ...sourceProps, ...(CarbonComponent.propTypes || {}) };
  const injectProps = compConfig.injectProps || {};
  const propMap = compConfig.propMap || {};
  
  const allProps = { ...carbonPropTypes };
  const fragmentDestructuring = [];
  const fragmentPassThrough = [];
  
  // Custom props take precedence or are added
  // However, we MUST NOT include id, children, className, or style here if they are already in allProps
  // to avoid duplication in Destructuring. 
  // We handle these 4 specifically.
  for (const [propName, propDef] of Object.entries(injectProps)) {
    if (['id', 'children', 'className', 'style'].includes(propName)) continue;
    allProps[propName] = propDef;
  }

  let fragmentCode = `import React from 'react';
import { ${name} as Carbon${name}${hasAILabel ? ', AILabel' : ''} } from '@carbon/react';

const ${name} = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
    // Explicitly destructure injected props for better handling in fragment
  for (const propName of Object.keys(injectProps)) {
    if (['id', 'children', 'className', 'style'].includes(propName)) continue;
    
    if (reservedKeywords.includes(propName)) {
        fragmentDestructuring.push(`${propName}_: ${propName}_alias`);
        fragmentPassThrough.push(`${propName}={${propName}_alias}`);
    } else {
        const carbonPropName = propMap[propName] || propName;
        fragmentDestructuring.push(propName);
        fragmentPassThrough.push(`${carbonPropName}={${propName}}`);
    }
  }

  fragmentCode += `        \${fragmentDestructuring.join(',\\n        ')}\${fragmentDestructuring.length > 0 ? ',' : ''}
        ...otherProps
    } = props;
`;

  const eventMap = compConfig.eventMap || {};
  for (const [eventName, updates] of Object.entries(eventMap)) {
    fragmentCode += `    const ${eventName} = (...args) => {
        if (setProps) {
            setProps({\n`;
    updates.forEach(update => {
      fragmentCode += `                ${update.prop}: ${update.value.replace(/arguments/g, 'args')},\n`;
    });
    fragmentCode += `            });
        }
    };\n\n`;
  }

  fragmentCode += `    return (
        <Carbon${name}
            id={id}
            className={className}
            style={style}
            \${fragmentPassThrough.join('\\n            ')}
`;
  
  for (const eventName of Object.keys(eventMap)) {
    fragmentCode += `            ${eventName}={${eventName}}\n`;
  }

  if (hasAILabel) {
    fragmentCode += `            decorator={ai_label ? <AILabel /> : undefined}\n`;
  }

  fragmentCode += `            {...otherProps}
        >
            {children}
        </Carbon${name}>
    );
};

${name}.defaultProps = {\n`;

  const defaultPropsLines = [];
  for (const [propName, propDef] of Object.entries(injectProps)) {
    let defVal = propDef.default;
    if (typeof defVal === 'string') {
        defVal = `'${defVal}'`;
    } else if (defVal === null) {
        defVal = 'null';
    } else if (Array.isArray(defVal)) {
        defVal = JSON.stringify(defVal);
    } else if (typeof defVal === 'object') {
        defVal = JSON.stringify(defVal);
    }
    defaultPropsLines.push(`    ${propName}: ${defVal}`);
  }
  fragmentCode += defaultPropsLines.join(',\n');
  fragmentCode += `\n};\n\nexport default ${name};\n`;

  await fs.writeFile(path.join(DEST_FRAGMENTS_DIR, `${name}.react.js`), fragmentCode);

  // Generate Component Wrapper (for dash-generate-components)
  let componentCode = `import React from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * ${name} is a wrapper for the Carbon ${name} component.
 */
const ${name} = (props) => {
    const RealComponent = LazyLoader['${name}'];
    if (!RealComponent) {
        return null;
    }

    return (
        <React.Suspense fallback={null}>
            <RealComponent {...props}/>
        </React.Suspense>
    );
};

${name}.defaultProps = {\n`;
  
  componentCode += defaultPropsLines.join(',\n');
  componentCode += `\n};\n\n${name}.propTypes = {\n`;
  componentCode += `    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * The content of the component.
     */
    children: PropTypes.node,

    /**
     * Specify a custom className to be applied to the component.
     */
    className: PropTypes.string,

    /**
     * Inline styles
     */
    style: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,\n\n`;

  for (const [propName, ptValue] of Object.entries(allProps)) {
    if (['id', 'children', 'className', 'style', 'setProps'].includes(propName)) continue;
    
    // Some prop names might be invalid JS identifiers (e.g. contain hyphens like 'aria-label')
    // and also invalid Python identifiers.
    // In React/JS we must wrap them in quotes.
    // In Python, we can't easily have them as keyword arguments if they have hyphens.
    // Dash's component generator might handle this, but if we are passing them
    // to Python as keyword arguments in the class definition, it will fail.
    // Actually, dash-generate-components should handle this by converting them
    // to underscores or something, but it seems it didn't in this case or
    // it's just passing them through.
    // Let's skip props with hyphens for now to avoid breaking the Python backend
    // unless we find a better way to map them.
    if (propName.includes('-')) continue;
    
    let pt = 'PropTypes.any';
    if (typeof ptValue === 'object' && ptValue.type) {
        if (ptValue.type === 'number') pt = 'PropTypes.number';
        if (ptValue.type === 'bool') pt = 'PropTypes.bool';
        if (ptValue.type === 'string') pt = 'PropTypes.string';
        if (ptValue.type === 'node') pt = 'PropTypes.node';
        if (ptValue.type === 'array') pt = 'PropTypes.array';
    } else if (ptValue && ptValue.isRequired !== undefined) {
        // This is a PropTypes validator
        // We can't easily detect the type from the validator function at runtime
        // without executing it or parsing its source, so 'any' is safest.
        pt = 'PropTypes.any';
    } else {
        pt = 'PropTypes.any';
    }
    
    const reservedKeywords = ['as', 'from', 'class', 'def', 'if', 'else', 'elif', 'for', 'while', 'try', 'except', 'finally', 'with', 'import', 'pass', 'break', 'continue', 'return', 'yield', 'lambda', 'and', 'or', 'not', 'is', 'in', 'del', 'global', 'nonlocal', 'assert', 'raise', 'True', 'False', 'None'];
    const pythonPropName = reservedKeywords.includes(propName) ? `${propName}_` : propName;
    
    // Check if we need to alias it in React for passing back to Carbon
    if (reservedKeywords.includes(propName)) {
        // We'll use a special prop name in the React side that matches the Python side
        // and map it back in the fragment.
        if (!fragmentDestructuring.includes(`${propName}_: ${propName}_alias`)) {
            fragmentDestructuring.push(`${propName}_: ${propName}_alias`);
            fragmentPassThrough.push(`${propName}={${propName}_alias}`);
        }
    } else {
        if (!fragmentDestructuring.includes(propName)) {
            fragmentDestructuring.push(propName);
        }
    }

    componentCode += `    /**\n     * ${propName}\n     */\n    ${pythonPropName}: ${pt},\n\n`;
  }

  componentCode += `};\n\nexport default ${name};\n\nexport const defaultProps = ${name}.defaultProps;\nexport const propTypes = ${name}.propTypes;\n`;
  
  await fs.writeFile(path.join(DEST_COMPONENTS_DIR, `${name}.react.js`), componentCode);

  // Generate Test
  if (compConfig.testStrategy && compConfig.testStrategy.skip) {
    console.log(`Skipping test for ${name}.`);
  } else if (compConfig.testStrategy) {
    const testCode = `import carbon_dash
from dash import Dash, html, Input, Output
import time

def test_${name.toLowerCase()}_interaction(dash_duo):
    app = Dash(__name__)

    app.layout = html.Div([
        carbon_dash.${name}(
            id='test-${name.toLowerCase()}',
            ${compConfig.testStrategy.type === 'click' && name === 'Button' ? "children='Click me!'," : ""}
            ${name === 'Dropdown' ? "items=['Option 1', 'Option 2']," : ""}
            ${name === 'Select' ? "children=[carbon_dash.SelectItem(text='Option 1', value='Option 1'), carbon_dash.SelectItem(text='Option 2', value='Option 2')]," : ""}
            ${name === 'RadioButtonGroup' ? "children=[carbon_dash.RadioButton(id='opt1', label='Opt 1', value='opt1'), carbon_dash.RadioButton(id='opt2', label='Opt 2', value='opt2')]," : ""}
            ${name === 'Grid' ? "children=[carbon_dash.Row(children=[carbon_dash.Column(children='Grid Item')])]," : ""}
            ${name === 'Accordion' ? "children=[carbon_dash.AccordionItem(title='Item 1', children='Content 1')]," : ""}
            ${name === 'Tabs' ? "children=[carbon_dash.TabList(children=[carbon_dash.Tab(label='Tab 1')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Panel 1')])]," : ""}
            ${name === 'TabList' ? "children=[carbon_dash.Tab(label='Tab 1')]," : ""}
            ${name === 'Breadcrumb' ? "children=[carbon_dash.BreadcrumbItem(children='Item 1'), carbon_dash.BreadcrumbItem(children='Item 2')]," : ""}
            ${name === 'ProgressIndicator' ? "children=[carbon_dash.ProgressStep(label='Step 1'), carbon_dash.ProgressStep(label='Step 2')]," : ""}
            ${name === 'Tooltip' ? "children='Hover me', label='Tooltip content'," : ""}
        ),
        html.Div(id='output', children='initial')
    ])

    @app.callback(
        Output('output', 'children'),
        Input('test-${name.toLowerCase()}', '${compConfig.testStrategy.targetProp || "id"}'),
        prevent_initial_call=True
    )
    def update_output(val):
        return str(val)

    dash_duo.start_server(app)

    ${name === 'Dropdown' ? `
    # Open dropdown
    dash_duo.driver.find_element("css selector", "#test-${name.toLowerCase()} button").click()
    # Wait for options and click first one
    time.sleep(1)
    dash_duo.driver.find_element("xpath", "//div[contains(@class, 'cds--list-box__menu-item__option') and text()='Option 1']").click()
    ` : compConfig.testStrategy.type === 'render' ? `
    dash_duo.wait_for_element("${compConfig.testStrategy.selector.replace(/"/g, '\\"')}")
    ` : `
    el = dash_duo.wait_for_element("${compConfig.testStrategy.selector.replace(/"/g, '\\"')}")
    ${compConfig.testStrategy.type === 'click' ? `dash_duo.driver.execute_script("arguments[0].click();", el)` : `el.send_keys('${compConfig.testStrategy.keys}')`}
    `}
    
    ${compConfig.testStrategy.type !== 'render' ? `dash_duo.wait_for_text_to_equal('#output', str(${compConfig.testStrategy.expectedValue === true ? 'True' : compConfig.testStrategy.expectedValue === false ? 'False' : `'${compConfig.testStrategy.expectedValue}'`}))` : ''}
`;
    await fs.writeFile(path.join(DEST_TESTS_DIR, `test_${name.toLowerCase()}.py`), testCode);
  }
}

async function main() {
  console.log('Starting Carbon Dash Automation Pipeline...');
  
  await fs.ensureDir(DEST_COMPONENTS_DIR);
  await fs.ensureDir(DEST_FRAGMENTS_DIR);
  await fs.ensureDir(DEST_TESTS_DIR);

  const carbon = require('@carbon/react');
  
  // Discover all components exported by @carbon/react, including unstable and preview prefixes
  const carbonExports = {};
  const seenNames = new Set();

  Object.keys(carbon).forEach(key => {
    if (typeof carbon[key] === 'function' || (typeof carbon[key] === 'object' && carbon[key] !== null && (carbon[key].$$typeof || carbon[key].render || carbon[key].propTypes))) {
        let cleanName = key;
        if (key.startsWith('unstable__')) cleanName = key.replace('unstable__', '');
        if (key.startsWith('preview__')) cleanName = key.replace('preview__', '');
        
        // Skip constants and small-caps exports
        if (/^[A-Z]/.test(cleanName)) {
            // macOS is case-insensitive, but we can have components that differ ONLY in case
            // or where one export shadows another during iteration.
            // We prioritize the one already in config, or the one without a prefix.
            const lowerName = cleanName.toLowerCase();
            if (seenNames.has(lowerName)) {
                const existingName = Object.keys(carbonExports).find(k => k.toLowerCase() === lowerName);
                console.warn(`Warning: Duplicate component name detected with different casing: ${cleanName} (already have ${existingName}). Skipping ${cleanName} to avoid file system conflicts.`);
                return;
            }
            seenNames.add(lowerName);
            carbonExports[cleanName] = carbon[key];
        }
    }
  });

  const allCarbonComponents = Object.keys(carbonExports);
  
  // Clean up all existing generated files first to ensure a perfectly clean state
  console.log('Cleaning up existing generated files...');
  [DEST_FRAGMENTS_DIR, DEST_COMPONENTS_DIR].forEach(dir => {
    if (fs.existsSync(dir)) {
      fs.readdirSync(dir).forEach(file => {
        if (file.endsWith('.react.js')) {
          fs.unlinkSync(path.join(dir, file));
        }
      });
    }
  });
  
  const pythonDir = path.resolve(__dirname, '../carbon_dash');
  if (fs.existsSync(pythonDir)) {
    fs.readdirSync(pythonDir).forEach(file => {
      // Delete camel-case Python files which are likely generated components
      if (file.endsWith('.py') && /^[A-Z]/.test(file)) {
        fs.unlinkSync(path.join(pythonDir, file));
      }
    });
  }

  // Merge config components with all other Carbon components
  const componentsToGenerate = new Set([
    ...Object.keys(config),
    ...allCarbonComponents
  ]);

  for (const name of Array.from(componentsToGenerate).sort()) {
    const CarbonComponent = carbonExports[name];
    if (!CarbonComponent) {
        console.warn(`Warning: Component ${name} not found in @carbon/react exports. Skipping.`);
        continue;
    }
    const compConfig = config[name] || {};
    await generateComponent(name, CarbonComponent, compConfig);
  }

  // Generate LazyLoader and index.js
  const finalComponents = Array.from(componentsToGenerate).filter(name => carbonExports[name]).sort();
  
  let lazyLoaderCode = `import React from 'react';\n\n`;
  finalComponents.forEach(c => {
    lazyLoaderCode += `export const ${c} = React.lazy(() => import(/* webpackChunkName: "${c}" */ './fragments/${c}.react'));\n`;
  });
  await fs.writeFile(path.join(__dirname, '../src/lib/LazyLoader.js'), lazyLoaderCode);

  let indexCode = `import './styles.scss';\nimport './LazyLoader';\n`;
  finalComponents.forEach(c => {
    indexCode += `import ${c} from './components/${c}.react';\n`;
  });
  indexCode += `\nexport {\n  ${finalComponents.join(',\n  ')}\n};\n`;
  await fs.writeFile(path.join(__dirname, '../src/lib/index.js'), indexCode);

  console.log(`Automation pipeline complete. Generated ${finalComponents.length} components.`);
}

main().catch(console.error);
