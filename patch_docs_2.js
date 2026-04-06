const fs = require('fs');
const file = 'scripts/generate-docs.js';
let content = fs.readFileSync(file, 'utf8');

content = content.replace(
  "let pythonDocs = `import carbon_dash",
  "let pythonDocs = `import carbon_dash\\nimport dash_iconify"
);

fs.writeFileSync(file, content);
