import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * FeatureFlags is a wrapper for the Carbon FeatureFlags component.
 */
export default class FeatureFlags extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['FeatureFlags'];
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

FeatureFlags.defaultProps = {
    className: '',
};

FeatureFlags.propTypes = {
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
     * flags
     */
    flags: PropTypes.any,

    /**
     * enableV12TileDefaultIcons
     */
    enableV12TileDefaultIcons: PropTypes.node,

    /**
     * enableV12TileRadioIcons
     */
    enableV12TileRadioIcons: PropTypes.node,

    /**
     * enableV12Overflowmenu
     */
    enableV12Overflowmenu: PropTypes.any,

    /**
     * enableTreeviewControllable
     */
    enableTreeviewControllable: PropTypes.any,

    /**
     * enableExperimentalFocusWrapWithoutSentinels
     */
    enableExperimentalFocusWrapWithoutSentinels: PropTypes.any,

    /**
     * enableFocusWrapWithoutSentinels
     */
    enableFocusWrapWithoutSentinels: PropTypes.any,

    /**
     * enableDialogElement
     */
    enableDialogElement: PropTypes.any,

    /**
     * enableV12DynamicFloatingStyles
     */
    enableV12DynamicFloatingStyles: PropTypes.any,

    /**
     * enableEnhancedFileUploader
     */
    enableEnhancedFileUploader: PropTypes.any,

    /**
     * enablePresence
     */
    enablePresence: PropTypes.any,

};
