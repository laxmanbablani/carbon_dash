const fs = require('fs');
let code = fs.readFileSync('scripts/generate.js', 'utf8');

// Replace pt = 'PropTypes.any'; with context-aware logic
code = code.replace(
  "pt = 'PropTypes.any';",
  "pt = (propName.toLowerCase().includes('icon') || propName === 'children' || propName === 'leftSection' || propName === 'rightSection') ? 'PropTypes.node' : 'PropTypes.any';"
);

// We should do it globally
code = code.replace(
  /pt = 'PropTypes\.any';/g,
  "pt = (propName.toLowerCase().includes('icon') || propName === 'children' || propName === 'leftSection' || propName === 'rightSection') ? 'PropTypes.node' : 'PropTypes.any';"
);

fs.writeFileSync('scripts/generate.js', code);
