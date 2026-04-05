const fs = require('fs');
const path = require('path');
const parser = require('@babel/parser');
const traverse = require('@babel/traverse').default;

const DOCS_DIR = 'docs';
if (!fs.existsSync(DOCS_DIR)) fs.mkdirSync(DOCS_DIR);

const carbonReact = require('@carbon/react');

const componentsDir = path.resolve('_ref/carbon-design-system/packages/react/src/components');
const componentFolders = fs.readdirSync(componentsDir).filter(f => fs.statSync(path.join(componentsDir, f)).isDirectory());

const components = [];

function escapePythonString(str) {
    if (typeof str !== 'string') return "''";
    return "'" + str.replace(/\\/g, '\\\\').replace(/'/g, "\\'").replace(/\n/g, '\\n') + "'";
}

function processJSXElement(node) {
    if (!node || node.type !== 'JSXElement') return null;
    
    const elementName = node.openingElement.name.name;
    if (!elementName) return null;

    let props = [];
    node.openingElement.attributes.forEach(attr => {
        if (attr.type === 'JSXAttribute' && attr.name && attr.name.name) {
            const name = attr.name.name;
            if (name.includes('-')) return; // skip dash props
            
            let valueStr = "True";
            if (attr.value) {
                if (attr.value.type === 'StringLiteral') {
                    valueStr = escapePythonString(attr.value.value);
                } else if (attr.value.type === 'JSXExpressionContainer') {
                    if (attr.value.expression.type === 'NumericLiteral') {
                        valueStr = attr.value.expression.value;
                    } else if (attr.value.expression.type === 'BooleanLiteral') {
                        valueStr = attr.value.expression.value ? "True" : "False";
                    } else if (attr.value.expression.type === 'StringLiteral') {
                        valueStr = escapePythonString(attr.value.expression.value);
                    } else {
                        // For complex expressions we just use empty string to avoid crashes
                        return; // skip prop
                    }
                }
            }
            props.push(`${name}=${valueStr}`);
        }
    });

    let children = [];
    node.children.forEach(child => {
        if (child.type === 'JSXText') {
            const text = child.value.trim();
            if (text) children.push(escapePythonString(text));
        } else if (child.type === 'JSXElement') {
            const childResult = processJSXElement(child);
            if (childResult) children.push(childResult);
        } else if (child.type === 'JSXExpressionContainer') {
            if (child.expression.type === 'StringLiteral') {
                children.push(escapePythonString(child.expression.value));
            } else if (child.expression.type === 'TemplateLiteral') {
                // very simple template literal extraction
                let str = '';
                child.expression.quasis.forEach(q => { str += q.value.raw; });
                if (str.trim()) children.push(escapePythonString(str.trim()));
            }
        }
    });

    let childrenStr = "";
    if (children.length === 1) {
        childrenStr = `children=${children[0]}`;
    } else if (children.length > 1) {
        childrenStr = `children=[${children.join(', ')}]`;
    }

    if (childrenStr) {
        props.push(childrenStr);
    }
    
    if (carbonReact[elementName] || carbonReact['unstable__' + elementName] || carbonReact['preview__' + elementName]) {
        // Filter props for carbon_dash components based on available propTypes
        const component = carbonReact[elementName] || carbonReact['unstable__' + elementName] || carbonReact['preview__' + elementName];
        const allowedProps = ["children", "className", "id", "style", "setProps", ...Object.keys(component.propTypes || {})];
        const filteredProps = props.filter(p => {
            const propName = p.split('=')[0];
            return allowedProps.includes(propName) || propName === 'children' || !p.includes('=');
        });
        return `carbon_dash.${elementName}(${filteredProps.join(', ')})`;
    }
    
    // Fallback to html.Div for unknown components to keep the app running
    // We filter out props that are not allowed on html.Div
    const allowedDivProps = ["accessKey", "children", "className", "contentEditable", "dir", "disable_n_clicks", "draggable", "hidden", "id", "key", "lang", "n_clicks", "n_clicks_timestamp", "role", "spellCheck", "style", "tabIndex", "title"];
    const filteredProps = props.filter(p => allowedDivProps.some(allowed => p.startsWith(allowed + '=')) || p.startsWith('aria-') || p.startsWith('data-') || !p.includes('='));
    return `html.Div(${filteredProps.join(', ')})`;
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
        let stories = [];
        storyFiles.forEach(file => {
            const content = fs.readFileSync(file, 'utf-8');
            try {
                const ast = parser.parse(content, {
                    sourceType: 'module',
                    plugins: ['jsx', 'typescript', 'classProperties', 'decorators-legacy']
                });
                
                traverse(ast, {
                    ExportNamedDeclaration(pathNode) {
                        if (pathNode.node.declaration && pathNode.node.declaration.type === 'VariableDeclaration') {
                            const declarations = pathNode.node.declaration.declarations;
                            declarations.forEach(decl => {
                                if (decl.id.type === 'Identifier') {
                                    const storyName = decl.id.name;
                                    if (storyName === 'Default' || storyName === 'Playground') return;
                                    
                                    // Try to find the returned JSX Element
                                    let jsxResult = null;
                                    if (decl.init && decl.init.type === 'ArrowFunctionExpression') {
                                        if (decl.init.body.type === 'JSXElement') {
                                            jsxResult = processJSXElement(decl.init.body);
                                        } else if (decl.init.body.type === 'BlockStatement') {
                                            const returnStmt = decl.init.body.body.find(stmt => stmt.type === 'ReturnStatement');
                                            if (returnStmt && returnStmt.argument && returnStmt.argument.type === 'JSXElement') {
                                                jsxResult = processJSXElement(returnStmt.argument);
                                            }
                                        }
                                    }
                                    
                                    if (jsxResult) {
                                        stories.push({ name: storyName, code: jsxResult });
                                    } else {
                                        stories.push({ name: storyName, code: null });
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
        
        if (stories.length > 0 && carbonReact[folder]) {
            components.push({
                name: folder,
                stories: stories
            });
        }
    }
}

// Generate Python Docs
let pythonDocs = `import carbon_dash
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
        
        if (storyObj.code) {
            // we have AST extracted code
            storyItems += `        ${storyObj.code},\n`;
        } else {
            // fallback
            let compToRender = comp.name;
            let props = `id='${comp.name.toLowerCase()}-${storyName.toLowerCase()}'`;
            if (comp.name === 'Button') {
                if (storyName.includes('Primary')) props += `, kind='primary', children='Primary'`;
                else if (storyName.includes('Secondary')) props += `, kind='secondary', children='Secondary'`;
                else if (storyName.includes('Tertiary')) props += `, kind='tertiary', children='Tertiary'`;
                else if (storyName.includes('Ghost')) props += `, kind='ghost', children='Ghost'`;
                else if (storyName.includes('Danger')) props += `, kind='danger', children='Danger'`;
                else if (storyName.includes('IconButton')) props += `, hasIconOnly=True, iconDescription='Icon'`;
                else if (storyName.includes('Skeleton')) { compToRender = 'ButtonSkeleton'; props += ``; }
                else props += `, children='${storyName}'`;
            } else {
                if (storyName.includes('Skeleton') && carbonReact[comp.name + 'Skeleton']) {
                    compToRender = comp.name + 'Skeleton';
                }
            }
            storyItems += `        carbon_dash.${compToRender}(${props}),\n`;
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
