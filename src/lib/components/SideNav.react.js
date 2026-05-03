import React from 'react';
import PropTypes from 'prop-types';
import { SideNav as CarbonSideNav } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const SideNav = (props) => {
    const {
        id, children, className = '', style = {}, loading_state,
        ariaLabel, ariaLabelledBy,
        expanded, isFixedNav, isRail, isPersistent,
        addFocusListeners, addMouseListeners,
        ...others
    } = props;
    const ariaProps = {};
    if (ariaLabel !== undefined) ariaProps['aria-label'] = ariaLabel;
    if (ariaLabelledBy !== undefined) ariaProps['aria-labelledby'] = ariaLabelledBy;

    return (
        <CarbonSideNav
            id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            expanded={expanded}
            isFixedNav={isFixedNav}
            isRail={isRail}
            isPersistent={isPersistent}
            addFocusListeners={addFocusListeners}
            addMouseListeners={addMouseListeners}
            {...ariaProps}
            {...others}
        >
            {children}
        </CarbonSideNav>
    );
};

SideNav.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * The content of the side navigation.
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
     * Required props for accessibility label on the underlying menu.
     * Provide an aria-label.
     */
    ariaLabel: PropTypes.string,

    /**
     * Required props for accessibility label on the underlying menu.
     * Provide an aria-labelledby.
     */
    ariaLabelledBy: PropTypes.string,

    /**
     * Specify whether focus and blur listeners are added. They are by default.
     */
    addFocusListeners: PropTypes.bool,

    /**
     * Specify whether mouse entry/exit listeners are added. They are by default.
     */
    addMouseListeners: PropTypes.bool,

    /**
     * If `true`, the SideNav will be open on initial render.
     */
    defaultExpanded: PropTypes.bool,

    /**
     * Specify the duration in milliseconds to delay before displaying the side navigation.
     */
    enterDelayMs: PropTypes.number,

    /**
     * If `true`, the SideNav will be expanded, otherwise it will be collapsed.
     * Using this prop causes SideNav to become a controlled component.
     */
    expanded: PropTypes.bool,

    /**
     * Provide the `href` to the id of the element on your package that is the main content.
     */
    href: PropTypes.string,

    /**
     * Specify if sideNav is a child of the header.
     */
    isChildOfHeader: PropTypes.bool,

    /**
     * Specify if sideNav is standalone.
     */
    isFixedNav: PropTypes.bool,

    /**
     * Specify if the sideNav will be persistent above the lg breakpoint.
     */
    isPersistent: PropTypes.bool,

    /**
     * Optional prop to display the side nav rail.
     */
    isRail: PropTypes.bool,

    /**
     * An optional listener that is called when the SideNav overlay is clicked.
     */
    onOverlayClick: PropTypes.func,

    /**
     * An optional listener that is called as a callback to collapse the SideNav.
     */
    onSideNavBlur: PropTypes.func,

    /**
     * An optional listener that is called when an event that would cause
     * toggling the SideNav occurs.
     */
    onToggle: PropTypes.func,
};

SideNav.defaultProps = {
    expanded: true,
    isFixedNav: false,
    isRail: false,
    isPersistent: true,
    addFocusListeners: true,
    addMouseListeners: true,
    isChildOfHeader: true,
};

export default SideNav;
