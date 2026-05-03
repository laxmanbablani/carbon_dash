import React from 'react';
import PropTypes from 'prop-types';
import { Stack as CarbonStack } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * Stack is a wrapper for the Carbon Stack component.
 * A layout utility that provides consistent spacing between child elements.
 */
const Stack = (props) => {
    const {
        id,
        children,
        className = '',
        style = {},
        loading_state,
        as: asElement = 'div',
        gap,
        orientation = 'vertical',
        ...others
    } = props;

    return (
        <CarbonStack
            id={id}
            className={className}
            style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            as={asElement}
            gap={gap}
            orientation={orientation}
            {...others}
        >
            {children}
        </CarbonStack>
    );
};

Stack.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

    /** The content of the stack */
    children: PropTypes.node,

    /** Custom CSS class */
    className: PropTypes.string,

    /** Inline styles */
    style: PropTypes.object,

    /** Dash loading state */
    loading_state: PropTypes.shape({
        is_loading: PropTypes.bool,
        prop_name: PropTypes.string,
        component_name: PropTypes.string,
    }),

    /** Provide a custom element type to render as the outermost element */
    as: PropTypes.oneOfType([PropTypes.string, PropTypes.elementType]),

    /** Provide either a custom value or a step from the spacing scale to be used as the gap in the layout (1-12) */
    gap: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),

    /** Specify the orientation of items in the Stack */
    orientation: PropTypes.oneOf(['horizontal', 'vertical']),
};

Stack.defaultProps = {
    as: 'div',
    orientation: 'vertical',
};

export default Stack;
