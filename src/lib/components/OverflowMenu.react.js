import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * OverflowMenu is a wrapper for the Carbon OverflowMenu component.
 */
export default class OverflowMenu extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['OverflowMenu'];
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

OverflowMenu.defaultProps = {
    className: '',
};

OverflowMenu.propTypes = {
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
     * align
     */
    align: PropTypes.any,

    /**
     * ariaLabel
     */
    ariaLabel: PropTypes.any,

    /**
     * direction
     */
    direction: PropTypes.any,

    /**
     * flipped
     */
    flipped: PropTypes.any,

    /**
     * focusTrap
     */
    focusTrap: PropTypes.any,

    /**
     * iconClass
     */
    iconClass: PropTypes.any,

    /**
     * iconDescription
     */
    iconDescription: PropTypes.any,

    /**
     * light
     */
    light: PropTypes.any,

    /**
     * menuOffset
     */
    menuOffset: PropTypes.any,

    /**
     * top
     */
    top: PropTypes.any,

    /**
     * left
     */
    left: PropTypes.any,

    /**
     * menuOffsetFlip
     */
    menuOffsetFlip: PropTypes.any,

    /**
     * menuOptionsClass
     */
    menuOptionsClass: PropTypes.any,

    /**
     * onClick
     */
    onClick: PropTypes.any,

    /**
     * onClose
     */
    onClose: PropTypes.any,

    /**
     * onFocus
     */
    onFocus: PropTypes.any,

    /**
     * onKeyDown
     */
    onKeyDown: PropTypes.any,

    /**
     * onOpen
     */
    onOpen: PropTypes.any,

    /**
     * open
     */
    open: PropTypes.any,

    /**
     * renderIcon
     */
    renderIcon: PropTypes.any,

    /**
     * selectorPrimaryFocus
     */
    selectorPrimaryFocus: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

};
