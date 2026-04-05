import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * HeaderName is a wrapper for the Carbon HeaderName component.
 */
export default class HeaderName extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['HeaderName'];
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

HeaderName.defaultProps = {
    className: '',
};

HeaderName.propTypes = {
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
     * href
     */
    href: PropTypes.any,

    /**
     * prefix
     */
    prefix: PropTypes.any,

};
