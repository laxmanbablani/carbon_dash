import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * FormGroup is a wrapper for the Carbon FormGroup component.
 */
export default class FormGroup extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['FormGroup'];
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

FormGroup.defaultProps = {
    className: '',
};

FormGroup.propTypes = {
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
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * invalid
     */
    invalid: PropTypes.any,

    /**
     * legendId
     */
    legendId: PropTypes.any,

    /**
     * legendText
     */
    legendText: PropTypes.any,

    /**
     * message
     */
    message: PropTypes.any,

    /**
     * messageText
     */
    messageText: PropTypes.any,

};
