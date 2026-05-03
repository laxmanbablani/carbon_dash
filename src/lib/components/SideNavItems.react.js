import React from 'react';
import PropTypes from 'prop-types';
import { SideNavItems as CarbonSideNavItems } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const SideNavItems = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;
    return (
        <CarbonSideNavItems
            id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonSideNavItems>
    );
};

SideNavItems.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Provide the children to be rendered inside of the SideNavItems.
     */
    children: PropTypes.node,

    /**
     * Custom CSS class.
     */
    className: PropTypes.string,

    /**
     * Inline styles.
     */
    style: PropTypes.object,

    /**
     * Dash loading state.
     */
    loading_state: PropTypes.shape({
        is_loading: PropTypes.bool,
        prop_name: PropTypes.string,
        component_name: PropTypes.string,
    }),

    /**
     * Property to indicate if the side nav container is open (or not).
     * Use to keep local state and styling in step with the SideNav expansion state.
     */
    isSideNavExpanded: PropTypes.bool,
};

export default SideNavItems;
