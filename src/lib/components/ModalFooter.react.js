import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * ModalFooter is a wrapper for the Carbon ModalFooter component.
 */
export default class ModalFooter extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['ModalFooter'];
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

ModalFooter.defaultProps = {
    className: '',
};

ModalFooter.propTypes = {
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
     * closeModal
     */
    closeModal: PropTypes.any,

    /**
     * danger
     */
    danger: PropTypes.any,

    /**
     * inputref
     */
    inputref: PropTypes.any,

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
     * primaryButtonDisabled
     */
    primaryButtonDisabled: PropTypes.any,

    /**
     * primaryButtonText
     */
    primaryButtonText: PropTypes.any,

    /**
     * primaryClassName
     */
    primaryClassName: PropTypes.any,

    /**
     * secondaryButtonText
     */
    secondaryButtonText: PropTypes.any,

    /**
     * secondaryButtons
     */
    secondaryButtons: PropTypes.any,

    /**
     * secondaryClassName
     */
    secondaryClassName: PropTypes.any,

};
