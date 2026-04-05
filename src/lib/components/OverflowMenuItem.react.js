import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * OverflowMenuItem is a wrapper for the Carbon OverflowMenuItem component.
 */
export default class OverflowMenuItem extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['OverflowMenuItem'];
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

OverflowMenuItem.defaultProps = {
    className: '',
};

OverflowMenuItem.propTypes = {
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
     * closeMenu
     */
    closeMenu: PropTypes.any,

    /**
     * dangerDescription
     */
    dangerDescription: PropTypes.any,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * handleOverflowMenuItemFocus
     */
    handleOverflowMenuItemFocus: PropTypes.any,

    /**
     * hasDivider
     */
    hasDivider: PropTypes.any,

    /**
     * href
     */
    href: PropTypes.any,

    /**
     * index
     */
    index: PropTypes.any,

    /**
     * isDelete
     */
    isDelete: PropTypes.any,

    /**
     * itemText
     */
    itemText: PropTypes.any,

    /**
     * onBlur
     */
    onBlur: PropTypes.any,

    /**
     * onClick
     */
    onClick: PropTypes.any,

    /**
     * onFocus
     */
    onFocus: PropTypes.any,

    /**
     * onKeyDown
     */
    onKeyDown: PropTypes.any,

    /**
     * onKeyUp
     */
    onKeyUp: PropTypes.any,

    /**
     * onMouseDown
     */
    onMouseDown: PropTypes.any,

    /**
     * onMouseEnter
     */
    onMouseEnter: PropTypes.any,

    /**
     * onMouseLeave
     */
    onMouseLeave: PropTypes.any,

    /**
     * onMouseUp
     */
    onMouseUp: PropTypes.any,

    /**
     * requireTitle
     */
    requireTitle: PropTypes.any,

    /**
     * title
     */
    title: PropTypes.any,

    /**
     * wrapperClassName
     */
    wrapperClassName: PropTypes.any,

};
