import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * IconButton is a wrapper for the Carbon IconButton component.
 */
export default class IconButton extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['IconButton'];
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

IconButton.defaultProps = {
    className: '',
};

IconButton.propTypes = {
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
     * autoAlign
     */
    autoAlign: PropTypes.any,

    /**
     * badgeCount
     */
    badgeCount: PropTypes.any,

    /**
     * href
     */
    href: PropTypes.any,

    /**
     * closeOnActivation
     */
    closeOnActivation: PropTypes.any,

    /**
     * defaultOpen
     */
    defaultOpen: PropTypes.any,

    /**
     * dropShadow
     */
    dropShadow: PropTypes.any,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * enterDelayMs
     */
    enterDelayMs: PropTypes.any,

    /**
     * isSelected
     */
    isSelected: PropTypes.any,

    /**
     * highContrast
     */
    highContrast: PropTypes.any,

    /**
     * kind
     */
    kind: PropTypes.any,

    /**
     * label
     */
    label: PropTypes.any,

    /**
     * leaveDelayMs
     */
    leaveDelayMs: PropTypes.any,

    /**
     * rel
     */
    rel: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

    /**
     * target
     */
    target: PropTypes.any,

    /**
     * wrapperClasses
     */
    wrapperClasses: PropTypes.any,

};
