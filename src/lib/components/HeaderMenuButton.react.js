import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * HeaderMenuButton is a wrapper for the Carbon HeaderMenuButton component.
 */
export default class HeaderMenuButton extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['HeaderMenuButton'];
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

HeaderMenuButton.defaultProps = {
    className: '',
};

HeaderMenuButton.propTypes = {
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
     * isCollapsible
     */
    isCollapsible: PropTypes.any,

    /**
     * onClick
     */
    onClick: PropTypes.any,

};
