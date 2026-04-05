import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * InlineLoading is a wrapper for the Carbon InlineLoading component.
 */
export default class InlineLoading extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['InlineLoading'];
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

InlineLoading.defaultProps = {
    className: '',
};

InlineLoading.propTypes = {
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
     * description
     */
    description: PropTypes.any,

    /**
     * iconDescription
     */
    iconDescription: PropTypes.any,

    /**
     * onSuccess
     */
    onSuccess: PropTypes.any,

    /**
     * status
     */
    status: PropTypes.any,

    /**
     * successDelay
     */
    successDelay: PropTypes.any,

};
