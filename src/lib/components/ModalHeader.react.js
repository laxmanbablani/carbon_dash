import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * ModalHeader is a wrapper for the Carbon ModalHeader component.
 */
export default class ModalHeader extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['ModalHeader'];
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

ModalHeader.defaultProps = {
    className: '',
};

ModalHeader.propTypes = {
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
     * buttonOnClick
     */
    buttonOnClick: PropTypes.any,

    /**
     * closeClassName
     */
    closeClassName: PropTypes.any,

    /**
     * closeIconClassName
     */
    closeIconClassName: PropTypes.node,

    /**
     * closeModal
     */
    closeModal: PropTypes.any,

    /**
     * iconDescription
     */
    iconDescription: PropTypes.any,

    /**
     * label
     */
    label: PropTypes.any,

    /**
     * labelClassName
     */
    labelClassName: PropTypes.any,

    /**
     * title
     */
    title: PropTypes.any,

    /**
     * titleClassName
     */
    titleClassName: PropTypes.any,

};
