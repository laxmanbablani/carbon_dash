import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * HeaderGlobalAction is a wrapper for the Carbon HeaderGlobalAction component.
 */
export default class HeaderGlobalAction extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['HeaderGlobalAction'];
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

HeaderGlobalAction.defaultProps = {
    className: '',
};

HeaderGlobalAction.propTypes = {
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
     * isActive
     */
    isActive: PropTypes.any,

    /**
     * onClick
     */
    onClick: PropTypes.any,

    /**
     * tooltipAlignment
     */
    tooltipAlignment: PropTypes.any,

    /**
     * tooltipDropShadow
     */
    tooltipDropShadow: PropTypes.any,

    /**
     * tooltipHighContrast
     */
    tooltipHighContrast: PropTypes.any,

};
