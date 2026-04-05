import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * HeaderMenu is a wrapper for the Carbon HeaderMenu component.
 */
export default class HeaderMenu extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['HeaderMenu'];
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

HeaderMenu.defaultProps = {
    className: '',
};

HeaderMenu.propTypes = {
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
     * focusRef
     */
    focusRef: PropTypes.any,

    /**
     * isActive
     */
    isActive: PropTypes.any,

    /**
     * isCurrentPage
     */
    isCurrentPage: PropTypes.any,

    /**
     * menuLinkName
     */
    menuLinkName: PropTypes.any,

    /**
     * onBlur
     */
    onBlur: PropTypes.any,

    /**
     * onClick
     */
    onClick: PropTypes.any,

    /**
     * onKeyDown
     */
    onKeyDown: PropTypes.any,

    /**
     * renderMenuContent
     */
    renderMenuContent: PropTypes.any,

    /**
     * tabIndex
     */
    tabIndex: PropTypes.any,

};
