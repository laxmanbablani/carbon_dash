import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * HeaderMenuItem is a wrapper for the Carbon HeaderMenuItem component.
 */
export default class HeaderMenuItem extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['HeaderMenuItem'];
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

HeaderMenuItem.defaultProps = {
    className: '',
};

HeaderMenuItem.propTypes = {
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
     * element
     */
    element: PropTypes.any,

    /**
     * isSideNavExpanded
     */
    isSideNavExpanded: PropTypes.any,

    /**
     * isActive
     */
    isActive: PropTypes.any,

    /**
     * isCurrentPage
     */
    isCurrentPage: PropTypes.any,

    /**
     * role
     */
    role: PropTypes.any,

    /**
     * tabIndex
     */
    tabIndex: PropTypes.any,

};
