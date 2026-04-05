import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Breadcrumb is a wrapper for the Carbon Breadcrumb component.
 */
export default class Breadcrumb extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { noTrailingSlash } = this.props;

        const RealComponent = LazyLoader['Breadcrumb'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    noTrailingSlash={noTrailingSlash}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

Breadcrumb.defaultProps = {
    className: '',
    noTrailingSlash: false,
};

Breadcrumb.propTypes = {
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
     * noTrailingSlash
     */
    noTrailingSlash: PropTypes.bool,

    /**
     * size
     */
    size: PropTypes.any,

};
