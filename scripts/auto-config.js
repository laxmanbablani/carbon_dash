const fs = require('fs');
const path = require('path');

const COMP_DIR = '_ref/carbon-design-system/packages/react/src/components';
const CONFIG_PATH = 'scripts/config.json';

const currentConfig = JSON.parse(fs.readFileSync(CONFIG_PATH, 'utf8'));

const components = fs.readdirSync(COMP_DIR).filter(f => {
    return fs.statSync(path.join(COMP_DIR, f)).isDirectory();
});

console.log(`Found ${components.length} components.`);

components.forEach(name => {
    if (currentConfig[name]) return;

    // Default configuration for new components
    currentConfig[name] = {
        "injectProps": {
            "className": { "type": "string", "default": "" }
        },
        "testStrategy": {
            "type": "render",
            "selector": ".cds--${name.toLowerCase()}"
        }
    };
    
    // Some basic heuristics
    if (name.includes('Skeleton')) {
        currentConfig[name].testStrategy.selector = `.cds--${name.toLowerCase().replace('skeleton', '-skeleton')}`;
    }
});

fs.writeFileSync(CONFIG_PATH, JSON.stringify(currentConfig, null, 2));
console.log('Updated scripts/config.json with missing components.');
