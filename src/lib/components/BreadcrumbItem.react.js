import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * BreadcrumbItem is a wrapper for the Carbon BreadcrumbItem component.
 */
export default class BreadcrumbItem extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { href } = this.props;
        const { isCurrentPage } = this.props;

        const RealComponent = LazyLoader['BreadcrumbItem'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    href={href}
                    isCurrentPage={isCurrentPage}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

BreadcrumbItem.defaultProps = {
    className: '',
    href: '#',
    isCurrentPage: false,
};

BreadcrumbItem.propTypes = {
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
     * href
     */
    href: PropTypes.string,

    /**
     * isCurrentPage
     */
    isCurrentPage: PropTypes.bool,

};
