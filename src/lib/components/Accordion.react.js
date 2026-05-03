import React from 'react';
import PropTypes from 'prop-types';
import { Accordion as CarbonAccordion } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * Accordion is a wrapper for the Carbon Accordion component.
 * Used for organizing content in collapsible panels.
 */
const Accordion = (props) => {
    const {
        id,
        children,
        className = '',
        style = {},
        loading_state,
        align = 'end',
        disabled = false,
        isFlush = false,
        ordered = false,
        size,
        ...others
    } = props;

    return (
        <CarbonAccordion
            id={id}
            className={className}
            style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            align={align}
            disabled={disabled}
            isFlush={isFlush}
            ordered={ordered}
            size={size}
            {...others}
        >
            {children}
        </CarbonAccordion>
    );
};

Accordion.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

    /** The content of the accordion (AccordionItem children) */
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

    /** Specify the alignment of the accordion heading title and chevron */
    align: PropTypes.oneOf(['start', 'end']),

    /** Specify whether an individual AccordionItem should be disabled */
    disabled: PropTypes.bool,

    /** Specify whether Accordion text should be flush, does not work with align="start" */
    isFlush: PropTypes.bool,

    /** Specify if the Accordion should be an ordered list */
    ordered: PropTypes.bool,

    /** Specify the size of the Accordion */
    size: PropTypes.oneOf(['sm', 'md', 'lg']),
};

Accordion.defaultProps = {
    align: 'end',
    disabled: false,
    isFlush: false,
    ordered: false,
};

export default Accordion;
