import React from 'react';
import PropTypes from 'prop-types';
import { TabPanels as CarbonTabPanels, TabPanel as CarbonTabPanel } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const TabPanels = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;
    return (
        <CarbonTabPanels
            id={id}
            className={className}
            style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonTabPanels>
    );
};

TabPanels.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,
    /** TabPanel components rendered inside this container */
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
};

export default TabPanels;
