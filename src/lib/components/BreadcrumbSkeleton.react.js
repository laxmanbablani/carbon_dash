import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * BreadcrumbSkeleton is a wrapper for the Carbon BreadcrumbSkeleton component.
 */
export default class BreadcrumbSkeleton extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['BreadcrumbSkeleton'];
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

BreadcrumbSkeleton.defaultProps = {
    className: '',
};

BreadcrumbSkeleton.propTypes = {
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
     * items
     */
    items: PropTypes.any,

    /**
     * noTrailingSlash
     */
    noTrailingSlash: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

};
