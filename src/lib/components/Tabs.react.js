import React from 'react';
import PropTypes from 'prop-types';
import { Tabs as CarbonTabs } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * Tabs is a wrapper for the Carbon Tabs component.
 * Provides a tabbed interface for organizing content.
 */
const Tabs = (props) => {
    const {
        id,
        children,
        className = '',
        style = {},
        loading_state,
        selectedIndex,
        defaultSelectedIndex = 0,
        ...others
    } = props;

    return (
        <CarbonTabs
            id={id}
            className={className}
            style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            selectedIndex={selectedIndex}
            defaultSelectedIndex={defaultSelectedIndex}
            {...others}
        >
            {children}
        </CarbonTabs>
    );
};

Tabs.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

    /** The content of the tabs (should contain TabList and TabPanels) */
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

    /** Control which content panel is currently selected */
    selectedIndex: PropTypes.number,

    /** Specify which content tab should be initially selected when the component is first rendered */
    defaultSelectedIndex: PropTypes.number,

    /** Whether the rendered Tab children should be dismissable */
    dismissable: PropTypes.bool,
};

Tabs.defaultProps = {
    defaultSelectedIndex: 0,
};

export default Tabs;
