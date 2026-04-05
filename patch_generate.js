const fs = require('fs');
let content = fs.readFileSync('scripts/generate.js', 'utf8');

// 1. Add definitions
const defs = `
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
`;

content = content.replace("const config = require('./config.json');", "const config = require('./config.json');\n" + defs);

// Replace hardcoded propTypes definition
const oldPropTypesBlock = `    /**
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

content = content.replace(oldPropTypesBlock, `    ...DashBaseProps,\n\n`);

// Add PersistenceProps and DebounceProps injection logic
const injectLogic = `
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
`;

// Insert the logic just before the props iteration for fragment Destructuring
content = content.replace("const fragmentDestructuring = [];", injectLogic + "\n  const fragmentDestructuring = [];");

// Replace the fragment props destructuring to include loading_state
content = content.replace(/className = \$\{defaultProps\.className \|\| "''"\},/g, "className = ${defaultProps.className || \"''\"},\n        loading_state,");

// Update the fragment return code to use data-dash-is-loading
content = content.replace(/<Carbon\$\{name\}/g, `<Carbon\${name}\n            data-dash-is-loading={(loading_state && loading_state.is_loading) || undefined}`);

// Ensure DashBaseProps string representation in the propTypes assignment
content = content.replace(/componentCode \+= \`    \.\.\.DashBaseProps,\\n\\n\`;/g, `
  componentCode += Object.entries(DashBaseProps).map(([k, v]) => \`    /** \${k} */\\n    \${k}: \${v},\`).join('\\n\\n') + '\\n\\n';
  if (needsPersistence) {
      componentCode += Object.entries(PersistenceProps).map(([k, v]) => \`    /** \${k} */\\n    \${k}: \${v},\`).join('\\n\\n') + '\\n\\n';
  }
  if (needsDebounce) {
      componentCode += Object.entries(DebounceProps).map(([k, v]) => \`    /** \${k} */\\n    \${k}: \${v},\`).join('\\n\\n') + '\\n\\n';
  }
`);

// Skip generating pt values for DashBaseProps, PersistenceProps, DebounceProps again
content = content.replace(
  "if (['id', 'children', 'className', 'style', 'setProps'].includes(propName)) continue;", 
  "if (Object.keys(DashBaseProps).includes(propName) || Object.keys(PersistenceProps).includes(propName) || Object.keys(DebounceProps).includes(propName)) continue;"
);

// We need a proper getLoadingState function in the fragment
const fragmentHeader = `import React from 'react';
import { \${name} as Carbon\${name}\${hasAILabel ? ', AILabel' : ''} } from '@carbon/react';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};
`;

content = content.replace(/import React from 'react';\nimport \{ \$\{name\} as Carbon\$\{name\}\$\{hasAILabel \? ', AILabel' : ''\} \} from '@carbon\/react';/g, fragmentHeader);

content = content.replace(/data-dash-is-loading=\{\(loading_state && loading_state\.is_loading\) \|\| undefined\}/g, "data-dash-is-loading={getLoadingState(loading_state)}");

// Handle fragment injected props iteration correctly
// The original code ignores ['id', 'children', 'className', 'style']
content = content.replace(/if \(\['id', 'children', 'className', 'style'\]\.includes\(propName\)\) continue;/g, "if (Object.keys(DashBaseProps).includes(propName)) continue;");


fs.writeFileSync('scripts/generate.js', content);
