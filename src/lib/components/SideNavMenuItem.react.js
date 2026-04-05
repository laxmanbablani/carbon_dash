import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * SideNavMenuItem is a wrapper for the Carbon SideNavMenuItem component.
 */
export default class SideNavMenuItem extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['SideNavMenuItem'];
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

SideNavMenuItem.defaultProps = {
    className: '',
};

SideNavMenuItem.propTypes = {
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
     * as
     */
    as_: PropTypes.any,

    /**
     * href
     */
    href: PropTypes.any,

    /**
     * isActive
     */
    isActive: PropTypes.any,

};
