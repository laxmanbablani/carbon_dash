import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Toggletip is a wrapper for the Carbon Toggletip component.
 */
export default class Toggletip extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['Toggletip'];
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

Toggletip.defaultProps = {
    className: '',
};

Toggletip.propTypes = {
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
     * defaultOpen
     */
    defaultOpen: PropTypes.any,

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

};
