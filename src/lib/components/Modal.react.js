import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Modal is a wrapper for the Carbon Modal component.
 */
export default class Modal extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { open } = this.props;
        const { modalHeading } = this.props;
        const { primaryButtonText } = this.props;
        const { secondaryButtonText } = this.props;

        const RealComponent = LazyLoader['Modal'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    open={open}
                    modalHeading={modalHeading}
                    primaryButtonText={primaryButtonText}
                    secondaryButtonText={secondaryButtonText}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

Modal.defaultProps = {
    className: '',
    open: false,
    modalHeading: 'Modal Heading',
    primaryButtonText: 'Primary Button',
    secondaryButtonText: 'Secondary Button',
};

Modal.propTypes = {
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

    /** persistence */
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),

    /** persisted_props */
    persisted_props: PropTypes.arrayOf(PropTypes.string),

    /** persistence_type */
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),

    /**
     * alert
     */
    alert: PropTypes.any,

    /**
     * closeButtonLabel
     */
    closeButtonLabel: PropTypes.any,

    /**
     * danger
     */
    danger: PropTypes.any,

    /**
     * decorator
     */
    decorator: PropTypes.any,

    /**
     * hasScrollingContent
     */
    hasScrollingContent: PropTypes.any,

    /**
     * isFullWidth
     */
    isFullWidth: PropTypes.any,

    /**
     * launcherButtonRef
     */
    launcherButtonRef: PropTypes.any,

    /**
     * current
     */
    current: PropTypes.any,

    /**
     * loadingDescription
     */
    loadingDescription: PropTypes.any,

    /**
     * loadingIconDescription
     */
    loadingIconDescription: PropTypes.any,

    /**
     * loadingStatus
     */
    loadingStatus: PropTypes.any,

    /**
     * modalAriaLabel
     */
    modalAriaLabel: PropTypes.any,

    /**
     * modalHeading
     */
    modalHeading: PropTypes.string,

    /**
     * modalLabel
     */
    modalLabel: PropTypes.any,

    /**
     * onKeyDown
     */
    onKeyDown: PropTypes.any,

    /**
     * onLoadingSuccess
     */
    onLoadingSuccess: PropTypes.any,

    /**
     * onRequestClose
     */
    onRequestClose: PropTypes.any,

    /**
     * onRequestSubmit
     */
    onRequestSubmit: PropTypes.any,

    /**
     * onSecondarySubmit
     */
    onSecondarySubmit: PropTypes.any,

    /**
     * open
     */
    open: PropTypes.bool,

    /**
     * passiveModal
     */
    passiveModal: PropTypes.any,

    /**
     * preventCloseOnClickOutside
     */
    preventCloseOnClickOutside: PropTypes.any,

    /**
     * primaryButtonDisabled
     */
    primaryButtonDisabled: PropTypes.any,

    /**
     * primaryButtonText
     */
    primaryButtonText: PropTypes.string,

    /**
     * secondaryButtonText
     */
    secondaryButtonText: PropTypes.string,

    /**
     * secondaryButtons
     */
    secondaryButtons: PropTypes.any,

    /**
     * selectorPrimaryFocus
     */
    selectorPrimaryFocus: PropTypes.any,

    /**
     * selectorsFloatingMenus
     */
    selectorsFloatingMenus: PropTypes.any,

    /**
     * shouldSubmitOnEnter
     */
    shouldSubmitOnEnter: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

    /**
     * slug
     */
    slug: PropTypes.any,

};
