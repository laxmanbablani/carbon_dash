import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Popover is a wrapper for the Carbon Popover component.
 */
export default class Popover extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['Popover'];
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

Popover.defaultProps = {
    className: '',
};

Popover.propTypes = {
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
     * alignmentAxisOffset
     */
    alignmentAxisOffset: PropTypes.any,

    /**
     * as
     */
    as_: PropTypes.any,

    /**
     * autoAlign
     */
    autoAlign: PropTypes.any,

    /**
     * backgroundToken
     */
    backgroundToken: PropTypes.any,

    /**
     * autoAlignBoundary
     */
    autoAlignBoundary: PropTypes.any,

    /**
     * x
     */
    x: PropTypes.any,

    /**
     * y
     */
    y: PropTypes.any,

    /**
     * width
     */
    width: PropTypes.any,

    /**
     * height
     */
    height: PropTypes.any,

    /**
     * caret
     */
    caret: PropTypes.any,

    /**
     * border
     */
    border: PropTypes.any,

    /**
     * dropShadow
     */
    dropShadow: PropTypes.any,

    /**
     * highContrast
     */
    highContrast: PropTypes.any,

    /**
     * isTabTip
     */
    isTabTip: PropTypes.any,

    /**
     * onRequestClose
     */
    onRequestClose: PropTypes.any,

    /**
     * open
     */
    open: PropTypes.any,

};
