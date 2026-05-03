import React from 'react';
import * as Icons from '@carbon/react/icons';

/**
 * Resolves an icon prop from Dash to a React element.
 * Handles: React elements, Carbon icon strings, DashIconify objects, plain objects.
 */
export const resolveIcon = (iconProp) => {
    if (iconProp === null || iconProp === undefined) return null;
    if (React.isValidElement(iconProp)) return iconProp;

    // Carbon icon by name (e.g. "Add", "Edit", "Launch")
    if (typeof iconProp === 'string') return Icons[iconProp] || null;

    // Serialized Dash component (DashIconify, html.Div, etc.)
    // Arrives as {type: "DashIconify", namespace: "dash_iconify", props: {icon: "carbon:launch"}}
    if (typeof iconProp === 'object' && iconProp.type && iconProp.namespace && iconProp.props) {
        try {
            const ns = window[iconProp.namespace];
            const Component = ns?.[iconProp.type];
            if (Component) return React.createElement(Component, iconProp.props);
        } catch (e) { }
    }

    return null;
};
