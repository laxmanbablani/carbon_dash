const fs = require('fs');
const path = require('path');
const parser = require('@babel/parser');
const traverse = require('@babel/traverse').default;

const DOCS_DIR = 'docs';
if (!fs.existsSync(DOCS_DIR)) fs.mkdirSync(DOCS_DIR);

const carbonReact = require('@carbon/react');
const carbonIcons = require('@carbon/react/icons');

const componentsDir = path.resolve('_ref/carbon-design-system/packages/react/src/components');
const componentFolders = fs.readdirSync(componentsDir).filter(f => fs.statSync(path.join(componentsDir, f)).isDirectory());

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

  const funcPattern = new RegExp(`(?:function|const)\\s+${name}(?:\\s*:[^=]+)?\\s*(?:=\\s*)?\\(\\s*{([^}]*)}\\s*\\)`, 's');
  const match = source.match(funcPattern);
  
  if (match && match[1]) {
    const propLines = match[1].split(',');
    propLines.forEach(line => {
        const cleanLine = line.replace(/\/\*.*?\*\/|\/\/.*/g, '').trim();
        const propMatch = cleanLine.match(/^([a-zA-Z0-9_]+)(?:\s*[:=]\s*.*)?$/);
        if (propMatch && propMatch[1] && propMatch[1] !== 'rest' && propMatch[1] !== 'other') {
            props[propMatch[1]] = 'any';
        }
    });
  }

  const interfacePattern = new RegExp(`(?:interface|type)\\s+${name}Props(?:\\s*=\\s*{|\\s*{)([^}]*)}`, 's');
  const interfaceMatch = source.match(interfacePattern);
  if (interfaceMatch && interfaceMatch[1]) {
    const ptLines = interfaceMatch[1].split('\n');
    ptLines.forEach(line => {
      const lineMatch = line.trim().match(/^([a-zA-Z0-9_]+)\??\s*:/);
      if (lineMatch && lineMatch[1]) {
        props[lineMatch[1]] = 'any';
      }
    });
  }

  const propTypesPattern = new RegExp(`${name}\\.propTypes\\s*=\\s*{([^}]*)}`, 's');
  const ptMatch = source.match(propTypesPattern);
  if (ptMatch && ptMatch[1]) {
    const ptLines = ptMatch[1].split('\n');
    ptLines.forEach(line => {
      const lineMatch = line.trim().match(/^([a-zA-Z0-9_]+)\s*:/);
      if (lineMatch && lineMatch[1]) {
        props[lineMatch[1]] = 'any';
      }
    });
  }

  return props;
}

const components = [];

const reservedKeywords = ['as', 'from', 'class', 'def', 'if', 'else', 'elif', 'for', 'while', 'try', 'except', 'finally', 'with', 'import', 'pass', 'break', 'continue', 'return', 'yield', 'lambda', 'and', 'or', 'not', 'is', 'in', 'del', 'global', 'nonlocal', 'assert', 'raise', 'True', 'False', 'None'];

function escapePythonString(str) {
    if (typeof str !== 'string') return "''";
    return "'" + str.replace(/\\/g, '\\\\').replace(/'/g, "\\'").replace(/\n/g, '\\n') + "'";
}

function processJSXElement(node, scope = {}) {
    if (!node) return null;
    if (node.type === 'JSXFragment') {
        const children = (node.children || []).map(c => {
            if (c.type === 'JSXElement' || c.type === 'JSXFragment') return processJSXElement(c, scope);
            if (c.type === 'JSXText') {
                const text = c.value.trim();
                if (!text) return null;
                return escapePythonString(text);
            }
            if (c.type === 'JSXExpressionContainer') {
                if (c.expression.type === 'StringLiteral') return escapePythonString(c.expression.value);
                if (c.expression.type === 'TemplateLiteral') {
                     // Simplified template literal handling
                     if (c.expression.quasis.length === 1) {
                         return escapePythonString(c.expression.quasis[0].value.raw);
                     }
                }
            }
            return null;
        }).filter(Boolean);
        if (children.length === 0) return null;
        if (children.length === 1) return children[0];
        // Flatten nested lists in fragment results
        let flattened = [];
        children.forEach(c => {
            if (c.startsWith('[') && c.endsWith(']')) {
                flattened.push(...c.substring(1, c.length - 1).split(',').map(s => s.trim()));
            } else {
                flattened.push(c);
            }
        });
        return `[${flattened.join(', ')}]`;
    }
    if (node.type !== 'JSXElement') return null;
    
    const openingEl = node.openingElement;
    if (!openingEl || !openingEl.name) return null;
    const elementName = openingEl.name.name;
    if (!elementName) return null;

    // Handle HeaderContainer render prop pattern in Dash
    if (elementName === 'HeaderContainer') {
        const renderAttr = openingEl.attributes.find(a => a.type === 'JSXAttribute' && a.name.name === 'render');
        if (renderAttr && renderAttr.value && renderAttr.value.type === 'JSXExpressionContainer') {
            const expr = renderAttr.value.expression;
            if (expr.type === 'ArrowFunctionExpression' || expr.type === 'FunctionExpression') {
                const body = expr.body;
                const inner = processJSXElement(body, scope);
                if (inner) {
                    return `carbon_dash.HeaderContainer(children=${inner})`;
                }
            }
        }
    }

    let props = [];
    openingEl.attributes.forEach(attr => {
        if (attr.type === 'JSXAttribute' && attr.name && attr.name.name) {
            const name = attr.name.name;
            if (name === 'render' && elementName === 'HeaderContainer') return;
            if (name.includes('-')) return; // skip dash props
            
            let valueStr = "True";
            if (attr.value) {
                if (attr.value.type === 'StringLiteral') {
                    if (['renderIcon', 'icon', 'defaultIcon', 'leftSection', 'rightSection'].includes(name) && carbonIcons[attr.value.value]) {
                        const iconKebab = attr.value.value.replace(/([a-z])([A-Z])/g, '$1-$2').toLowerCase();
                        valueStr = `dash_iconify.DashIconify(icon="carbon:${iconKebab}")`;
                    } else {
                        valueStr = escapePythonString(attr.value.value);
                    }
                } else if (attr.value.type === 'JSXExpressionContainer') {
                    if (attr.value.expression.type === 'NumericLiteral') {
                        valueStr = attr.value.expression.value;
                    } else if (attr.value.expression.type === 'BooleanLiteral') {
                        valueStr = attr.value.expression.value ? "True" : "False";
                    } else if (attr.value.expression.type === 'StringLiteral') {
                        valueStr = escapePythonString(attr.value.expression.value);
                    } else if (attr.value.expression.type === 'Identifier') {
                        const idName = attr.value.expression.name;
                        if (carbonIcons[idName]) {
                            const iconKebab = idName.replace(/([a-z])([A-Z])/g, '$1-$2').toLowerCase();
                            valueStr = `dash_iconify.DashIconify(icon="carbon:${iconKebab}")`;
                        } else if (scope[idName]) {
                            valueStr = scope[idName];
                        } else {
                            return; // skip prop
                        }
                    } else if (attr.value.expression.type === 'ArrayExpression') {
                        const items = attr.value.expression.elements.map(el => {
                            if (el.type === 'StringLiteral') return escapePythonString(el.value);
                            if (el.type === 'NumericLiteral') return el.value;
                            if (el.type === 'ObjectExpression') return processObjectExpression(el, scope);
                            return null;
                        }).filter(item => item !== null);
                        valueStr = `[${items.join(', ')}]`;
                    } else if (attr.value.expression.type === 'ObjectExpression') {
                        valueStr = processObjectExpression(attr.value.expression, scope);
                    } else {
                        return; // skip prop
                    }
                }
            }
            const reservedKeywords = ['as', 'from', 'class', 'def', 'if', 'else', 'elif', 'for', 'while', 'try', 'except', 'finally', 'with', 'import', 'pass', 'break', 'continue', 'return', 'yield', 'lambda', 'and', 'or', 'not', 'is', 'in', 'del', 'global', 'nonlocal', 'assert', 'raise', 'True', 'False', 'None'];
            const pythonName = reservedKeywords.includes(name) ? `${name}_` : name;
            props.push(`${pythonName}=${valueStr}`);
        }
    });

    let children = [];
    node.children.forEach(child => {
        if (child.type === 'JSXText') {
            const text = child.value.trim();
            if (text) children.push(escapePythonString(text));
        } else if (child.type === 'JSXElement') {
            const childResult = processJSXElement(child, scope);
            if (childResult) {
                if (Array.isArray(childResult)) children.push(...childResult);
                else children.push(childResult);
            }
        } else if (child.type === 'JSXExpressionContainer') {
            if (child.expression.type === 'StringLiteral') {
                children.push(escapePythonString(child.expression.value));
            } else if (child.expression.type === 'TemplateLiteral') {
                // very simple template literal extraction
                let str = '';
                child.expression.quasis.forEach(q => { str += q.value.raw; });
                if (str.trim()) children.push(escapePythonString(str.trim()));
            } else if (child.expression.type === 'Identifier' && scope[child.expression.name]) {
                children.push(scope[child.expression.name]);
            }
        }
    });

    let childrenStr = "";
    if (children.length === 1) {
        childrenStr = `children=${children[0]}`;
    } else if (children.length > 1) {
        // Flatten nested lists in children
        let flattened = [];
        children.forEach(c => {
            if (c.startsWith('[') && c.endsWith(']')) {
                // very simple split that might fail on deep nesting but should help
                flattened.push(...c.substring(1, c.length - 1).split(',').map(s => s.trim()));
            } else {
                flattened.push(c);
            }
        });
        childrenStr = `children=[${flattened.join(', ')}]`;
    }

    if (childrenStr) {
        props.push(childrenStr);
    }
    
    if (carbonReact[elementName] || carbonReact['unstable__' + elementName] || carbonReact['preview__' + elementName]) {
        const compInCarbon = carbonReact[elementName] || carbonReact['unstable__' + elementName] || carbonReact['preview__' + elementName];
        
        // Final sanity check: Is this component actually generated and exported by carbon_dash?
        const generatedComponents = fs.readdirSync(path.resolve(__dirname, '../carbon_dash')).map(f => f.replace('.py', ''));
        if (!generatedComponents.includes(elementName)) {
            console.warn(`Warning: Component ${elementName} is in @carbon/react but not generated in carbon_dash. Skipping.`);
            return null;
        }

        // Filter props for carbon_dash components based on available propTypes
        const component = carbonReact[elementName] || carbonReact['unstable__' + elementName] || carbonReact['preview__' + elementName];
        const sourceProps = extractPropsFromSource(elementName);
        const allProps = { ...sourceProps, ...(component ? (component.propTypes || {}) : {}) };
        
        const allowedProps = ["children", "className", "id", "style", "setProps", ...Object.keys(allProps)].map(p => reservedKeywords.includes(p) ? `${p}_` : p);
        const filteredProps = props.filter(p => {
            if (!p.includes('=')) return true; // positional or already formatted
            const propName = p.split('=')[0].trim();
            return allowedProps.includes(propName) || propName === 'children';
        });

        // Special handling for DataTable data requirements
        if (elementName === 'DataTable' && !filteredProps.some(p => p.startsWith('rows='))) {
            filteredProps.push("rows=[{'id': 'a', 'name': 'Load Balancer 3', 'status': 'Disabled'}, {'id': 'b', 'name': 'Load Balancer 1', 'status': 'Starting'}]");
            if (!filteredProps.some(p => p.startsWith('headers='))) {
                filteredProps.push("headers=[{'key': 'name', 'header': 'Name'}, {'key': 'status', 'header': 'Status'}]");
            }
        }

        // Special handling for DatePicker requirements
        if ((elementName === 'DatePicker' || elementName === 'FluidDatePicker') && !filteredProps.some(p => p.startsWith('children='))) {
            const inputComp = elementName === 'DatePicker' ? 'DatePickerInput' : 'FluidDatePickerInput';
            filteredProps.push(`children=[carbon_dash.${inputComp}(id='${elementName.toLowerCase()}-input', labelText='Date Picker label', placeholder='mm/dd/yyyy')]`);
        }

        return `carbon_dash.${elementName}(${filteredProps.join(', ')})`;
    }
    
    // NO FALLBACK - if it's not a Carbon component we know about, it fails fast
    if (carbonIcons[elementName]) {
        const iconKebab = elementName.replace(/([a-z])([A-Z])/g, '$1-$2').toLowerCase();
        return `dash_iconify.DashIconify(icon="carbon:${iconKebab}")`;
    }
    console.warn(`Warning: Unknown component ${elementName} encountered in stories. Skipping.`);
    return null;
}

function processObjectExpression(node, scope) {
    const props = node.properties.map(p => {
        if (p.type !== 'ObjectProperty') return null;
        const key = p.key.name || p.key.value;
        let val = null;
        if (p.value.type === 'StringLiteral') val = escapePythonString(p.value.value);
        else if (p.value.type === 'NumericLiteral') val = p.value.value;
        else if (p.value.type === 'BooleanLiteral') val = p.value.value ? 'True' : 'False';
        else if (p.value.type === 'Identifier' && scope[p.value.name]) val = scope[p.value.name];
        else if (p.value.type === 'ArrayExpression') {
            const items = p.value.elements.map(el => {
                if (el.type === 'StringLiteral') return escapePythonString(el.value);
                if (el.type === 'NumericLiteral') return el.value;
                return null;
            }).filter(i => i !== null);
            val = `[${items.join(', ')}]`;
        }
        if (key && val !== null) return `'${key}': ${val}`;
        return null;
    }).filter(p => p !== null);
    return `{${props.join(', ')}}`;
}

for (const folder of componentFolders) {
    let storyFiles = [];
    const findStories = (dir) => {
        if (!fs.existsSync(dir)) return;
        fs.readdirSync(dir).forEach(file => {
            const fullPath = path.join(dir, file);
            if (fs.statSync(fullPath).isDirectory()) {
                findStories(fullPath);
            } else if (fullPath.includes('.stories.js') || fullPath.includes('.stories.tsx')) {
                storyFiles.push(fullPath);
            }
        });
    };
    findStories(path.join(componentsDir, folder));
    
    if (storyFiles.length > 0) {
        const stories = [];
        storyFiles.forEach(file => {
            const content = fs.readFileSync(file, 'utf-8');
            try {
                const ast = parser.parse(content, {
                    sourceType: 'module',
                    plugins: ['jsx', 'typescript', 'classProperties', 'decorators-legacy']
                });
                
                let localScope = {};
                traverse(ast, {
                    ExportNamedDeclaration(pathNode) {
                        if (pathNode.node.declaration && pathNode.node.declaration.type === 'VariableDeclaration') {
                            const decl = pathNode.node.declaration.declarations[0];
                            if (decl.id.type === 'Identifier' && decl.init) {
                                const storyName = decl.id.name;
                                if (storyName.startsWith('_')) return; // skip internal
                                
                                let storyNode = decl.init;
                                let args = null;
                                
                                if (storyNode.type === 'ArrowFunctionExpression' || storyNode.type === 'FunctionExpression') {
                                    args = storyNode.params[0] && storyNode.params[0].name;
                                    storyNode = storyNode.body;
                                }

                                if (storyNode.type === 'JSXElement' || storyNode.type === 'JSXFragment') {
                                    const code = processJSXElement(storyNode, localScope);
                                    if (code) {
                                        stories.push({ name: storyName, code });
                                    }
                                } else if (storyName && decl.init.type === 'ObjectExpression') {
                                    // CSF 3.0
                                    const renderProp = decl.init.properties.find(p => p.key && p.key.name === 'render');
                                    if (renderProp && (renderProp.value.type === 'ArrowFunctionExpression' || renderProp.value.type === 'FunctionExpression')) {
                                        const body = renderProp.value.body;
                                        const code = processJSXElement(body, localScope);
                                        if (code) {
                                            stories.push({ name: storyName, code });
                                        }
                                    }
                                }
                            }
                        }
                    },
                    VariableDeclarator(pathNode) {
                        if (pathNode.node.id.type === 'Identifier' && pathNode.node.init) {
                            const name = pathNode.node.id.name;
                            if (pathNode.node.init.type === 'ArrayExpression') {
                                const items = pathNode.node.init.elements.map(el => {
                                    if (el.type === 'ObjectExpression') return processObjectExpression(el, {});
                                    if (el.type === 'StringLiteral') return escapePythonString(el.value);
                                    if (el.type === 'NumericLiteral') return el.value;
                                    return null;
                                }).filter(i => i !== null);
                                localScope[name] = `[${items.join(', ')}]`;
                            } else if (pathNode.node.init.type === 'ObjectExpression') {
                                localScope[name] = processObjectExpression(pathNode.node.init, {});
                            } else if (pathNode.node.init.type === 'StringLiteral') {
                                localScope[name] = escapePythonString(pathNode.node.init.value);
                            }
                        }
                    },
                    AssignmentExpression(pathNode) {
                        // Capture Story.args = { ... }
                        if (
                            pathNode.node.left.type === 'MemberExpression' &&
                            pathNode.node.left.property.name === 'args' &&
                            pathNode.node.right.type === 'ObjectExpression'
                        ) {
                            const storyName = pathNode.node.left.object.name;
                            const args = {};
                            pathNode.node.right.properties.forEach(prop => {
                                if (prop.key && prop.key.name && prop.value) {
                                    const reservedKeywords = ['as', 'from', 'class', 'def', 'if', 'else', 'elif', 'for', 'while', 'try', 'except', 'finally', 'with', 'import', 'pass', 'break', 'continue', 'return', 'yield', 'lambda', 'and', 'or', 'not', 'is', 'in', 'del', 'global', 'nonlocal', 'assert', 'raise', 'True', 'False', 'None'];
                                    const pythonName = reservedKeywords.includes(prop.key.name) ? `${prop.key.name}_` : prop.key.name;
                                    if (prop.value.type === 'StringLiteral') {
                                        args[pythonName] = escapePythonString(prop.value.value);
                                    } else if (prop.value.type === 'BooleanLiteral') {
                                        args[pythonName] = prop.value.value ? 'True' : 'False';
                                    } else if (prop.value.type === 'NumericLiteral') {
                                        args[pythonName] = prop.value.value;
                                    }
                                }
                            });
                            
                            const existingStory = stories.find(s => s.name === storyName);
                            if (existingStory) {
                                existingStory.args = args;
                            } else {
                                stories.push({ name: storyName, args: args, code: null });
                            }
                        }
                    },
                    ExportNamedDeclaration(pathNode) {
                        if (pathNode.node.declaration && pathNode.node.declaration.type === 'VariableDeclaration') {
                            const declarations = pathNode.node.declaration.declarations;
                            declarations.forEach(decl => {
                                if (decl.id.type === 'Identifier') {
                                    const storyName = decl.id.name;
                                    if (storyName === 'Default' || storyName === 'Playground' || storyName === 'meta') return;
                                    
                                    // Try to find variables defined within the story function
                                    let storyScope = { ...localScope };
                                    if (decl.init && decl.init.type === 'ArrowFunctionExpression' && decl.init.body.type === 'BlockStatement') {
                                        decl.init.body.body.forEach(stmt => {
                                            if (stmt.type === 'VariableDeclaration') {
                                                stmt.declarations.forEach(d => {
                                                    if (d.id.type === 'Identifier' && d.init) {
                                                        if (d.init.type === 'ArrayExpression') {
                                                            const items = d.init.elements.map(el => {
                                                                if (el.type === 'ObjectExpression') return processObjectExpression(el, {});
                                                                if (el.type === 'StringLiteral') return escapePythonString(el.value);
                                                                if (el.type === 'NumericLiteral') return el.value;
                                                                return null;
                                                            }).filter(i => i !== null);
                                                            storyScope[d.id.name] = `[${items.join(', ')}]`;
                                                        } else if (d.init.type === 'ObjectExpression') {
                                                            storyScope[d.id.name] = processObjectExpression(d.init, {});
                                                        } else if (d.init.type === 'StringLiteral') {
                                                            storyScope[d.id.name] = escapePythonString(d.init.value);
                                                        }
                                                    }
                                                });
                                            }
                                        });
                                    }

                                    // Try to find the returned JSX Element
                                    let jsxResult = null;
                                    if (decl.init && decl.init.type === 'ArrowFunctionExpression') {
                                        if (decl.init.body.type === 'JSXElement' || decl.init.body.type === 'JSXFragment') {
                                            jsxResult = processJSXElement(decl.init.body, storyScope);
                                        } else if (decl.init.body.type === 'BlockStatement') {
                                            const returnStmt = decl.init.body.body.find(stmt => stmt.type === 'ReturnStatement');
                                            if (returnStmt && returnStmt.argument && (returnStmt.argument.type === 'JSXElement' || returnStmt.argument.type === 'JSXFragment')) {
                                                jsxResult = processJSXElement(returnStmt.argument, storyScope);
                                            }
                                        }
                                    } else if (decl.init && (decl.init.type === 'JSXElement' || decl.init.type === 'JSXFragment')) {
                                        jsxResult = processJSXElement(decl.init, storyScope);
                                    }
                                    
                                    if (jsxResult) {
                                        // Detect component name from JSX result if it's like carbon_dash.Name(...)
                                        let detectedComponent = folder;
                                        const matchName = jsxResult.match(/carbon_dash\.([a-zA-Z0-9_]+)/);
                                        if (matchName) detectedComponent = matchName[1];

                                        const existingComp = components.find(c => c.name === detectedComponent);
                                        if (existingComp) {
                                            existingComp.stories.push({ name: storyName, code: jsxResult });
                                        } else {
                                            components.push({ name: detectedComponent, stories: [{ name: storyName, code: jsxResult }] });
                                        }
                                    } else {
                                        // ... existing code for non-JSX stories if needed ...
                                    }
                                }
                            });
                        }
                    }
                });
            } catch (e) {
                // Ignore parse errors for some complex files
            }
        });
        
        if (stories.length > 0) {
            // Already handled by component detection inside traverse
        }
    }
}

// Generate Python Docs
let pythonDocs = `import carbon_dash\nimport dash_iconify
from dash import Dash, html, dcc, Input, Output

app = Dash(__name__)

# Component Stories
stories_dict = {}

`;

components.forEach(comp => {
    let storyItems = `html.Div([
        html.H2("${comp.name}"),
`;
    // Filter duplicates and default
    const uniqueStoriesMap = new Map();
    comp.stories.forEach(s => {
        if (!uniqueStoriesMap.has(s.name) || s.code) {
            uniqueStoriesMap.set(s.name, s);
        }
    });
    
    uniqueStoriesMap.forEach((storyObj, storyName) => {
        storyItems += `        html.H3("${storyName}"),\n`;
        
        let compToRender = comp.name;
        if (comp.name === 'Button' && storyName.includes('Skeleton')) {
            compToRender = 'ButtonSkeleton';
        } else if (storyName.includes('Skeleton') && carbonReact[comp.name + 'Skeleton']) {
            compToRender = comp.name + 'Skeleton';
        }

        let propsList = [];
        if (storyObj.args) {
            const component = carbonReact[compToRender] || carbonReact['unstable__' + compToRender] || carbonReact['preview__' + compToRender];
            const sourceProps = extractPropsFromSource(compToRender);
            const allProps = { ...sourceProps, ...(component ? (component.propTypes || {}) : {}) };
            const allowedProps = ["children", "className", "id", "style", "setProps", ...Object.keys(allProps)].map(p => reservedKeywords.includes(p) ? `${p}_` : p);

            Object.entries(storyObj.args).forEach(([k, v]) => {
                if (allowedProps.includes(k)) {
                    propsList.push(`${k}=${v}`);
                }
            });
        }

        if (storyObj.code) {
            // we have AST extracted code
            if (propsList.length > 0) {
                // If we have extracted code AND story args, we attempt to merge.
                // storyObj.code looks like "carbon_dash.Button(...)" or "[Comp1, Comp2]"
                let code = storyObj.code;
                if (code.startsWith('carbon_dash.') && code.endsWith(')')) {
                    let inside = code.substring(code.indexOf('(') + 1, code.length - 1);
                    let existingProps = inside.split(',').map(p => p.trim()).filter(p => p);
                    propsList.forEach(p => {
                        let propName = p.split('=')[0];
                        if (!existingProps.some(ep => ep.startsWith(propName + '='))) {
                            existingProps.push(p);
                        }
                    });
                    storyItems += `        html.Div(children=${code.substring(0, code.indexOf('(') + 1)}${existingProps.join(', ')}), style={'marginBottom': '20px'}),\n`;
                } else if (code.startsWith('[') && code.endsWith(']')) {
                    storyItems += `        html.Div(children=${storyObj.code}, style={'marginBottom': '20px'}),\n`;
                } else {
                    storyItems += `        html.Div(children=[${storyObj.code}], style={'marginBottom': '20px'}),\n`;
                }
            } else {
                let code = storyObj.code;
                if (code.startsWith('[') && code.endsWith(']')) {
                    storyItems += `        html.Div(children=${storyObj.code}, style={'marginBottom': '20px'}),\n`;
                } else {
                    storyItems += `        html.Div(children=[${storyObj.code}], style={'marginBottom': '20px'}),\n`;
                }
            }
        } else {
            // fallback
            let compToRender = comp.name;
            let idProp = `id='${comp.name.toLowerCase()}-${storyName.toLowerCase()}'`;
            if (!propsList.some(p => p.startsWith('id='))) {
                propsList.push(idProp);
            }
            if (comp.name === 'Button') {
                if (storyName.includes('Primary') && !propsList.some(p => p.startsWith('kind='))) propsList.push(`kind='primary'`);
                else if (storyName.includes('Secondary') && !propsList.some(p => p.startsWith('kind='))) propsList.push(`kind='secondary'`);
                else if (storyName.includes('Tertiary') && !propsList.some(p => p.startsWith('kind='))) propsList.push(`kind='tertiary'`);
                else if (storyName.includes('Ghost') && !propsList.some(p => p.startsWith('kind='))) propsList.push(`kind='ghost'`);
                else if (storyName.includes('Danger') && !propsList.some(p => p.startsWith('kind='))) propsList.push(`kind='danger'`);
                
                if (storyName.includes('IconButton')) {
                   if (!propsList.some(p => p.startsWith('hasIconOnly='))) propsList.push(`hasIconOnly=True`);
                   if (!propsList.some(p => p.startsWith('iconDescription='))) propsList.push(`iconDescription='Icon'`);
                }
                
                if (compToRender === 'Button') {
                    if (!propsList.some(p => p.startsWith('children='))) propsList.push(`children='${storyName}'`);
                }
            }
            storyItems += `        html.Div(children=[carbon_dash.${compToRender}(${propsList.join(', ')})], style={'marginBottom': '20px'}),\n`;
        }
    });
    storyItems += `    ])`;
    pythonDocs += `stories_dict['node-${comp.name.toLowerCase()}'] = ${storyItems}\n\n`;
});

pythonDocs += `
app.layout = html.Div([
    html.Div([
        carbon_dash.TreeView(
            id='component-tree',
            label='Carbon Components',
            children=[
                carbon_dash.TreeNode(
                    id='node-components',
                    label='Components',
                    isExpanded=True,
                    children=[
`;

// Sort components by name
components.sort((a, b) => a.name.localeCompare(b.name));

components.forEach((comp, index) => {
    pythonDocs += `                        carbon_dash.TreeNode(
                            id='node-${comp.name.toLowerCase()}',
                            label='${comp.name}',
                            value='${comp.name}'
                        )${index < components.length - 1 ? ',' : ''}
`;
});

pythonDocs += `                    ]
                )
            ]
        )
    ], style={'width': '250px', 'borderRight': '1px solid #ccc', 'padding': '20px', 'height': '100vh', 'overflowY': 'auto', 'position': 'fixed'}),
    
    html.Div(
        id='main-content',
        style={'marginLeft': '290px', 'padding': '40px'}
    )
])

@app.callback(
    Output('main-content', 'children'),
    Input('component-tree', 'active')
)
def render_content(active_node):
    if active_node in stories_dict:
        return stories_dict[active_node]
    return html.Div([
        html.H2("Carbon Dash Component Gallery"),
        html.P("Select a component from the tree on the left to view its stories and API.")
    ])

if __name__ == "__main__":
    import sys
    port = 8052
    if len(sys.argv) > 1 and sys.argv[1] == "--port":
        port = int(sys.argv[2])
    app.run(debug=True, port=port)
`;

fs.writeFileSync(path.join(DOCS_DIR, 'gallery.py'), pythonDocs);
console.log('Gallery app generated in docs/gallery.py with full automated story parsing');
