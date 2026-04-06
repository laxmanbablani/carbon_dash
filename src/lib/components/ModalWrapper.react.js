import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * ModalWrapper is a wrapper for the Carbon ModalWrapper component.
 */
export default class ModalWrapper extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['ModalWrapper'];
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

ModalWrapper.defaultProps = {
    className: '',
};

ModalWrapper.propTypes = {
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
     * buttonTriggerClassName
     */
    buttonTriggerClassName: PropTypes.any,

    /**
     * buttonTriggerText
     */
    buttonTriggerText: PropTypes.any,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * handleOpen
     */
    handleOpen: PropTypes.any,

    /**
     * handleSubmit
     */
    handleSubmit: PropTypes.any,

    /**
     * modalBeforeContent
     */
    modalBeforeContent: PropTypes.any,

    /**
     * modalHeading
     */
    modalHeading: PropTypes.any,

    /**
     * modalLabel
     */
    modalLabel: PropTypes.any,

    /**
     * modalText
     */
    modalText: PropTypes.any,

    /**
     * onKeyDown
     */
    onKeyDown: PropTypes.any,

    /**
     * passiveModal
     */
    passiveModal: PropTypes.any,

    /**
     * preventCloseOnClickOutside
     */
    preventCloseOnClickOutside: PropTypes.any,

    /**
     * primaryButtonText
     */
    primaryButtonText: PropTypes.any,

    /**
     * renderTriggerButtonIcon
     */
    renderTriggerButtonIcon: PropTypes.node,

    /**
     * secondaryButtonText
     */
    secondaryButtonText: PropTypes.any,

    /**
     * selectorPrimaryFocus
     */
    selectorPrimaryFocus: PropTypes.any,

    /**
     * shouldCloseAfterSubmit
     */
    shouldCloseAfterSubmit: PropTypes.any,

    /**
     * status
     */
    status: PropTypes.any,

    /**
     * triggerButtonIconDescription
     */
    triggerButtonIconDescription: PropTypes.any,

    /**
     * triggerButtonKind
     */
    triggerButtonKind: PropTypes.any,

    /**
     * withHeader
     */
    withHeader: PropTypes.any,

};
