import React from 'react';
import PropTypes from 'prop-types';
import { AccordionItem as CarbonAccordionItem } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * AccordionItem is a wrapper for the Carbon AccordionItem component.
 * Represents a single collapsible section within an Accordion.
 */
const AccordionItem = (props) => {
    const {
        id,
        children,
        className = '',
        style = {},
        loading_state,
        title = 'title',
        open = false,
        ...others
    } = props;

    return (
        <CarbonAccordionItem
            id={id}
            className={className}
            style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            title={title}
            open={open}
            {...others}
        >
            {children}
        </CarbonAccordionItem>
    );
};

AccordionItem.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

    /** The content of the accordion item */
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

    /** The accordion title */
    title: PropTypes.node,

    /** Whether the accordion item is open */
    open: PropTypes.bool,

    /** Specify whether an individual AccordionItem should be disabled */
    disabled: PropTypes.bool,
};

AccordionItem.defaultProps = {
    title: 'title',
    open: false,
};

export default AccordionItem;
