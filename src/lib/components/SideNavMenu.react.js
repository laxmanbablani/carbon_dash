import React from 'react';
import PropTypes from 'prop-types';
import { SideNavMenu as CarbonSideNavMenu } from '@carbon/react';
import { getLoadingState } from '../utils/dash';
import { resolveIcon } from '../utils/resolveIcon';

const SideNavMenu = (props) => {
    const {
        id, children, className = '', style = {}, loading_state,
        renderIcon,
        ...others
    } = props;
    const iconElement = resolveIcon(renderIcon);

    return (
        <CarbonSideNavMenu
            id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            renderIcon={iconElement}
            {...others}
        >
            {children}
        </CarbonSideNavMenu>
    );
};

SideNavMenu.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Provide SideNavMenuItem's inside of the SideNavMenu.
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
     * Specify whether the menu should default to expanded. By default, it will be closed.
     */
    defaultExpanded: PropTypes.bool,

    /**
     * Specify whether the SideNavMenu is "active".
     * SideNavMenu should be considered active if one of its menu items are a link for the current page.
     */
    isActive: PropTypes.bool,

    /**
     * Property to indicate if the side nav container is open (or not).
     * Use to keep local state and styling in step with the SideNav expansion state.
     */
    isSideNavExpanded: PropTypes.bool,

    /**
     * Specify if this is a large variation of the SideNavMenu.
     */
    large: PropTypes.bool,

    /**
     * An icon component to render in the menu.
     * Accepts DashIconify, html.Div, Carbon icon name string, or any React node.
     */
    renderIcon: PropTypes.node,

    /**
     * Optional prop to specify the tabIndex of the button.
     */
    tabIndex: PropTypes.number,

    /**
     * Provide the text for the overall menu name.
     */
    title: PropTypes.string,
};

export default SideNavMenu;
