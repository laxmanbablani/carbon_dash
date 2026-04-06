const fs = require('fs');
let code = fs.readFileSync('scripts/generate-docs.js', 'utf8');

// We need to inject the icons check
code = code.replace(
  "const carbonReact = require('@carbon/react');",
  "const carbonReact = require('@carbon/react');\nconst carbonIcons = require('@carbon/react/icons');"
);

// We replace the fallback I added back to checking if it's an icon
code = code.replace(
  /if \(\/\^\[A-Z\]\/\.test\(elementName\)\) \{\s*const iconKebab = elementName\.replace\(\/\(\[a-z\]\)\(\[A-Z\]\)\/g, '\$1-\$2'\)\.toLowerCase\(\);\s*return \`dash_iconify\.DashIconify\(icon="carbon:\$\{iconKebab\}"\)\`;\s*\}/g,
  `if (carbonIcons[elementName]) {
        const iconKebab = elementName.replace(/([a-z])([A-Z])/g, '$1-$2').toLowerCase();
        return \`dash_iconify.DashIconify(icon="carbon:\${iconKebab}")\`;
    }`
);

// Also for identifiers, check if it's in carbonIcons
code = code.replace(
  /if \(\/\^\[A-Z\]\/\.test\(idName\) && idName !== 'True' && idName !== 'False'\)/g,
  "if (carbonIcons[idName])"
);

fs.writeFileSync('scripts/generate-docs.js', code);
