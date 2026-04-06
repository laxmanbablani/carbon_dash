const fs = require('fs');
const file = 'scripts/generate-docs.js';
let content = fs.readFileSync(file, 'utf8');

// 1. Add dash_iconify import in the generated python output
content = content.replace(
  "import carbon_dash\nfrom dash import html",
  "import carbon_dash\nfrom dash import html\nimport dash_iconify"
);

// 2. Update processJSXElement to handle Identifier in JSXExpressionContainer
content = content.replace(
  "return; // skip prop",
  `if (attr.value.expression.type === 'Identifier') {
                            const idName = attr.value.expression.name;
                            if (/^[A-Z]/.test(idName) && idName !== 'True' && idName !== 'False') {
                                const iconKebab = idName.replace(/([a-z])([A-Z])/g, '$1-$2').toLowerCase();
                                valueStr = \`dash_iconify.DashIconify(icon="carbon:\${iconKebab}")\`;
                            } else {
                                return;
                            }
                        } else {
                            return; // skip prop
                        }`
);

// 3. Handle <Icon /> elements
content = content.replace(
  "console.warn(`Warning: Unknown component ${elementName} encountered in stories. Skipping.`);",
  `if (/^[A-Z]/.test(elementName)) {
        const iconKebab = elementName.replace(/([a-z])([A-Z])/g, '$1-$2').toLowerCase();
        return \`dash_iconify.DashIconify(icon="carbon:\${iconKebab}")\`;
    }
    console.warn(\`Warning: Unknown component \${elementName} encountered in stories. Skipping.\`);`
);

fs.writeFileSync(file, content);
