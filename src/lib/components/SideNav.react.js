import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * SideNav is a wrapper for the Carbon SideNav component.
 */
export default class SideNav extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { expanded } = this.props;

        const RealComponent = LazyLoader['SideNav'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    expanded={expanded}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

SideNav.defaultProps = {
    className: '',
    expanded: false,
};

SideNav.propTypes = {
    /** id */
    id: PropTypes.string,

    /** children */
    children: PropTypes.node,

    /** className */
    className: PropTypes.string,

    /** style */
    style: PropTypes.object,

    /** setProps */
    setProps: PropTypes.func,

    /** loading_state */
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),

    /**
     * addFocusListeners
     */
    addFocusListeners: PropTypes.any,

    /**
     * addMouseListeners
     */
    addMouseListeners: PropTypes.any,

    /**
     * defaultExpanded
     */
    defaultExpanded: PropTypes.any,

    /**
     * enterDelayMs
     */
    enterDelayMs: PropTypes.any,

    /**
     * expanded
     */
    expanded: PropTypes.bool,

    /**
     * href
     */
    href: PropTypes.any,

    /**
     * isChildOfHeader
     */
    isChildOfHeader: PropTypes.any,

    /**
     * isFixedNav
     */
    isFixedNav: PropTypes.any,

    /**
     * isPersistent
     */
    isPersistent: PropTypes.any,

    /**
     * isRail
     */
    isRail: PropTypes.any,

    /**
     * onOverlayClick
     */
    onOverlayClick: PropTypes.any,

    /**
     * onSideNavBlur
     */
    onSideNavBlur: PropTypes.any,

    /**
     * onToggle
     */
    onToggle: PropTypes.any,

};
