import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * SideNavMenu is a wrapper for the Carbon SideNavMenu component.
 */
export default class SideNavMenu extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['SideNavMenu'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

SideNavMenu.defaultProps = {
    className: '',
};

SideNavMenu.propTypes = {
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
     * defaultExpanded
     */
    defaultExpanded: PropTypes.any,

    /**
     * isActive
     */
    isActive: PropTypes.any,

    /**
     * isSideNavExpanded
     */
    isSideNavExpanded: PropTypes.any,

    /**
     * large
     */
    large: PropTypes.any,

    /**
     * renderIcon
     */
    renderIcon: PropTypes.node,

    /**
     * tabIndex
     */
    tabIndex: PropTypes.any,

    /**
     * title
     */
    title: PropTypes.any,

};
