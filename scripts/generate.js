const fs = require('fs-extra');
const path = require('path');
const config = require('./config.json');

const DashBaseProps = {
    /** The ID used to identify this component in Dash callbacks. */
    id: 'PropTypes.string',
    /** The content of the component. */
    children: 'PropTypes.node',
    /** Specify a custom className to be applied to the component. */
    className: 'PropTypes.string',
    /** Inline styles */
    style: 'PropTypes.object',
    /** Dash-assigned callback that should be called to report property changes */
    setProps: 'PropTypes.func',
    /** Object that holds the loading state object coming from dash-renderer */
    loading_state: 'PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string })'
};

const PersistenceProps = {
    /** Used to allow user interactions in this component to be persisted */
    persistence: 'PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number])',
    /** Properties whose user interactions will persist */
    persisted_props: 'PropTypes.arrayOf(PropTypes.string)',
    /** Where persisted user changes will be stored */
    persistence_type: "PropTypes.oneOf(['local', 'session', 'memory'])"
};

const DebounceProps = {
    /** An integer that represents the number of times that this element has lost focus */
    n_blur: 'PropTypes.number',
    /** An integer that represents the number of times that this element has been submitted */
    n_submit: 'PropTypes.number',
    /** If True, changes to input will be sent back to the Dash server only on enter or when losing focus. */
    debounce: 'PropTypes.oneOfType([PropTypes.bool, PropTypes.number])'
};


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
  if (!fs.existsSync(componentDir)) return { props: {}, defaults: {} };

  const files = fs.readdirSync(componentDir);
  const targetFile = isSkeleton 
    ? files.find(f => f.toLowerCase().includes('skeleton') && (f.endsWith('.tsx') || f.endsWith('.js')))
    : files.find(f => (f === `${baseName}.tsx` || f === `${baseName}.js` || f === 'index.tsx' || f === 'index.js'));

  if (!targetFile) return { props: {}, defaults: {} };

  const source = fs.readFileSync(path.join(componentDir, targetFile), 'utf8');
  const props = {};
  const defaults = {};

  // Regex to find props in function signature: function Component({ prop1, prop2 = default })
  // This is a simplified regex but should capture most destructured props in Carbon
  const funcPattern = new RegExp(`(?:function|const)\\s+${name}(?:\\s*:[^=]+)?\\s*(?:=\\s*)?\\(\\s*{([^}]*)}\\s*\\)`, 's');
  const match = source.match(funcPattern);
  
  if (match && match[1]) {
    const propLines = match[1].split(',');
    propLines.forEach(line => {
        // Strip comments and handle { prop: alias }
        const cleanLine = line.replace(/\/\*.*?\*\/|\/\/.*/g, '').trim();
        // Match prop and optional default value
        const propMatch = cleanLine.match(/^([a-zA-Z0-9_]+)(?:\s*[:=]\s*([^,]+))?$/);
        if (propMatch && propMatch[1] && propMatch[1] !== 'rest' && propMatch[1] !== 'other') {
            const pName = propMatch[1];
            props[pName] = 'PropTypes.any';
            if (propMatch[2]) {
                let defVal = propMatch[2].trim();
                // Basic cleanup of common defaults
                if (defVal === 'true' || defVal === 'false' || !isNaN(defVal) || (defVal.startsWith("'") && defVal.endsWith("'")) || (defVal.startsWith('"') && defVal.endsWith('"'))) {
                    defaults[pName] = defVal;
                }
            }
        }
    });
  }

  // Also look for defaultProps definition in source
  const defaultPropsPattern = new RegExp(`${name}\\.defaultProps\\s*=\\s*{([^}]*)}`, 's');
  const dpMatch = source.match(defaultPropsPattern);
  if (dpMatch && dpMatch[1]) {
    const dpLines = dpMatch[1].split('\n');
    dpLines.forEach(line => {
      const lineMatch = line.trim().match(/^([a-zA-Z0-9_]+)\s*:\s*([^,]+)/);
      if (lineMatch && lineMatch[1]) {
        let defVal = lineMatch[2].trim();
        if (defVal.endsWith(',')) defVal = defVal.slice(0, -1).trim();
        defaults[lineMatch[1]] = defVal;
      }
    });
  }

  // Also look for TypeScript interface/type definitions
  const interfacePattern = new RegExp(`(?:interface|type)\\s+${name}Props(?:\\s*=\\s*{|\\s*{)([^}]*)}`, 's');
  const interfaceMatch = source.match(interfacePattern);
  if (interfaceMatch && interfaceMatch[1]) {
    const ptLines = interfaceMatch[1].split('\n');
    ptLines.forEach(line => {
      // prop?: type or prop: type
      const lineMatch = line.trim().match(/^([a-zA-Z0-9_]+)\??\s*:/);
      if (lineMatch && lineMatch[1]) {
        props[lineMatch[1]] = 'PropTypes.any';
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

  return { props, defaults };
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
  const { props: sourceProps, defaults: sourceDefaults } = extractPropsFromSource(name);
  const carbonPropTypes = { ...sourceProps, ...(CarbonComponent.propTypes || {}) };
  const injectProps = compConfig.injectProps || {};
  const propMap = compConfig.propMap || {};
  
  const allProps = { ...carbonPropTypes };
  
  let isInteractive = compConfig.eventMap && Object.keys(compConfig.eventMap).length > 0;
  let hasValue = allProps.hasOwnProperty('value') || allProps.hasOwnProperty('checked');
  let needsPersistence = isInteractive || hasValue;
  let needsDebounce = hasValue; // Simplified, typically inputs

  if (needsPersistence) {
      Object.assign(allProps, PersistenceProps);
  }
  if (needsDebounce) {
      Object.assign(allProps, DebounceProps);
  }
  Object.assign(allProps, DashBaseProps); // Ensure DashBaseProps are in allProps for prop iteration

  // Ensure sensible defaults for interactive props to prevent controlled/uncontrolled warnings
  if (allProps.hasOwnProperty('value') && !injectProps.hasOwnProperty('value') && sourceDefaults.value === undefined) {
      injectProps['value'] = { type: 'any', default: null };
  }
  if (allProps.hasOwnProperty('checked') && !injectProps.hasOwnProperty('checked') && sourceDefaults.checked === undefined) {
      injectProps['checked'] = { type: 'bool', default: false };
  }
  if (allProps.hasOwnProperty('selectedItem') && !injectProps.hasOwnProperty('selectedItem') && sourceDefaults.selectedItem === undefined) {
      injectProps['selectedItem'] = { type: 'any', default: null };
  }
  if (allProps.hasOwnProperty('toggled') && !injectProps.hasOwnProperty('toggled') && sourceDefaults.toggled === undefined) {
      injectProps['toggled'] = { type: 'bool', default: false };
  }

  const fragmentDestructuring = [];
  const fragmentPassThrough = [];
  
  // Custom props take precedence or are added
  // However, we MUST NOT include id, children, className, or style here if they are already in allProps
  // to avoid duplication in Destructuring. 
  // We handle these 4 specifically.
  for (const [propName, propDef] of Object.entries(injectProps)) {
    if (Object.keys(DashBaseProps).includes(propName)) continue;
    allProps[propName] = propDef;
  }

  const reservedKeywords = ['as', 'from', 'class', 'def', 'if', 'else', 'elif', 'for', 'while', 'try', 'except', 'finally', 'with', 'import', 'pass', 'break', 'continue', 'return', 'yield', 'lambda', 'and', 'or', 'not', 'is', 'in', 'del', 'global', 'nonlocal', 'assert', 'raise', 'True', 'False', 'None'];

  const defaultProps = { ...sourceDefaults };
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
    defaultProps[propName] = defVal;
  }

  let fragmentCode = `import React from 'react';
import { ${name} as Carbon${name}${hasAILabel ? ', AILabel' : ''} } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const ${name} = (props) => {
    const {
        id,
        setProps,
        children,
        className = ${defaultProps.className || "''"},
        loading_state,
        style,
`;

  // Explicitly destructure injected props for better handling in fragment
  for (const propName of Object.keys(injectProps)) {
    if (Object.keys(DashBaseProps).includes(propName)) continue;
    
    if (reservedKeywords.includes(propName)) {
        fragmentDestructuring.push(`${propName}_: ${propName}_alias = ${defaultProps[propName]}`);
        if (['renderIcon', 'icon', 'defaultIcon', 'leftSection', 'rightSection'].includes(propName)) {
            fragmentPassThrough.push(`${propName}={resolveIcon(${propName}_alias)}`);
        } else {
            fragmentPassThrough.push(`${propName}={${propName}_alias}`);
        }
    } else {
        const carbonPropName = propMap[propName] || propName;
        fragmentDestructuring.push(`${propName} = ${defaultProps[propName]}`);
        if (['renderIcon', 'icon', 'defaultIcon', 'leftSection', 'rightSection'].includes(propName)) {
            fragmentPassThrough.push(`${carbonPropName}={resolveIcon(${propName})}`);
        } else {
            fragmentPassThrough.push(`${carbonPropName}={${propName}}`);
        }
    }
  }

  fragmentCode += `        ${fragmentDestructuring.join(',\n        ')}${fragmentDestructuring.length > 0 ? ',' : ''}
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
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            ${fragmentPassThrough.join('\n            ')}
`;
  
  for (const eventName of Object.keys(eventMap)) {
    fragmentCode += `            ${eventName}={${eventName}}\n`;
  }

  // Pass remaining injected props except ai_label (if it maps to decorator)
  // These are now handled in fragmentPassThrough
  
  fragmentCode += `            {...otherProps}
        >
            {children}
        </Carbon${name}>
    );
};

export default ${name};
`;

  // Only generate a new fragment if it doesn't already exist or we want to overwrite it
  // Actually, we should probably keep custom fragments and only generate if missing
  const fragmentPath = path.join(DEST_FRAGMENTS_DIR, `${name}.react.js`);
  if (!fs.existsSync(fragmentPath)) {
    console.log(`  Generating NEW fragment for ${name}...`);
    await fs.writeFile(fragmentPath, fragmentCode);
  } else {
    console.log(`  Skipping fragment generation for ${name} (custom fragment exists).`);
  }

  // Generate Component Wrapper (for dash-generate-components)
  let componentCode = `import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * ${name} is a wrapper for the Carbon ${name} component.
 */
export default class ${name} extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
`;

  for (const propName of Object.keys(injectProps)) {
      if (Object.keys(DashBaseProps).includes(propName)) continue;
      componentCode += `        const { ${propName} } = this.props;\n`;
  }

  componentCode += `
        const RealComponent = LazyLoader['${name}'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
`;

  for (const propName of Object.keys(injectProps)) {
      if (Object.keys(DashBaseProps).includes(propName)) continue;
      componentCode += `                    ${propName}={${propName}}\n`;
  }

  componentCode += `                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

${name}.defaultProps = {
    className: ${defaultProps.className || "''"},\n`;
  
  for (const propName of Object.keys(injectProps)) {
      if (Object.keys(DashBaseProps).includes(propName)) continue;
      componentCode += `    ${propName}: ${defaultProps[propName]},\n`;
  }

  componentCode += `};\n\n`;

  componentCode += `${name}.propTypes = {\n`;
  componentCode += Object.entries(DashBaseProps).map(([k, v]) => `    /** ${k} */\n    ${k}: ${v},`).join('\n\n') + '\n\n';
  if (needsPersistence) {
      componentCode += Object.entries(PersistenceProps).map(([k, v]) => `    /** ${k} */\n    ${k}: ${v},`).join('\n\n') + '\n\n';
  }
  if (needsDebounce) {
      componentCode += Object.entries(DebounceProps).map(([k, v]) => `    /** ${k} */\n    ${k}: ${v},`).join('\n\n') + '\n\n';
  }

  for (const [propName, ptValue] of Object.entries(allProps)) {
    if (Object.keys(DashBaseProps).includes(propName) || Object.keys(PersistenceProps).includes(propName) || Object.keys(DebounceProps).includes(propName)) continue;
    
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
    
    let pt = ((propName.toLowerCase().includes('icon') && !propName.startsWith('has') && !propName.startsWith('is') && !propName.includes('Description')) || propName === 'children' || propName === 'leftSection' || propName === 'rightSection') ? 'PropTypes.node' : 'PropTypes.any';
    if (typeof ptValue === 'string' && ptValue.startsWith('PropTypes')) {
        pt = ptValue;
    } else if (typeof ptValue === 'object' && ptValue.type) {
        if (ptValue.type === 'number') pt = 'PropTypes.number';
        if (ptValue.type === 'bool') pt = 'PropTypes.bool';
        if (ptValue.type === 'string') pt = 'PropTypes.string';
        if (ptValue.type === 'node') pt = 'PropTypes.node';
        if (ptValue.type === 'array') pt = 'PropTypes.array';
    } else if (ptValue && ptValue.isRequired !== undefined) {
        pt = ((propName.toLowerCase().includes('icon') && !propName.startsWith('has') && !propName.startsWith('is') && !propName.includes('Description')) || propName === 'children' || propName === 'leftSection' || propName === 'rightSection') ? 'PropTypes.node' : 'PropTypes.any';
    } else {
        pt = ((propName.toLowerCase().includes('icon') && !propName.startsWith('has') && !propName.startsWith('is') && !propName.includes('Description')) || propName === 'children' || propName === 'leftSection' || propName === 'rightSection') ? 'PropTypes.node' : 'PropTypes.any';
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
            const carbonPropName = propMap[propName] || propName;
            fragmentPassThrough.push(`${carbonPropName}={${propName}}`);
        }
    }

    componentCode += `    /**\n     * ${propName}\n     */\n    ${pythonPropName}: ${pt},\n\n`;
  }

  componentCode += `};\n`;
  
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
  [DEST_COMPONENTS_DIR].forEach(dir => {
    if (fs.existsSync(dir)) {
      fs.readdirSync(dir).forEach(file => {
        if (file.endsWith('.react.js')) {
          fs.unlinkSync(path.join(dir, file));
        }
      });
    }
  });
  
  // Only cleanup fragments if they are NOT custom
  // Actually, we'll let the generator handle it (it won't overwrite existing ones)
  // For now, let's keep all fragments to be safe, but this might lead to stale fragments.
  // Ideally, fragments would have a header indicating if they were auto-generated.
  // For this project, we'll assume anything in fragments that we want to keep was manually edited.
  
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
