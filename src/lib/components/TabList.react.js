import React from 'react';
import PropTypes from 'prop-types';
import { TabList as CarbonTabList } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const TabList = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;
    return (
        <CarbonTabList
            id={id}
            className={className}
            style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonTabList>
    );
};

TabList.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,
    /** Tab components rendered inside this list */
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
    /** Specify whether the tab list should be contained */
    contained: PropTypes.bool,
    /** Specify whether the tab list should be full width */
    fullWidth: PropTypes.bool,
    /** Specify the activation mode. 'automatic' or 'manual' */
    activation: PropTypes.oneOf(['automatic', 'manual']),
    /** Specify the label used for the tab list aria-label */
    ariaLabel: PropTypes.string,
};

TabList.defaultProps = {
    contained: false,
    fullWidth: false,
    activation: 'automatic',
};

export default TabList;
