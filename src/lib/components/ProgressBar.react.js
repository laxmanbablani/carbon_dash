import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * ProgressBar is a wrapper for the Carbon ProgressBar component.
 */
export default class ProgressBar extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['ProgressBar'];
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

ProgressBar.defaultProps = {
    className: '',
};

ProgressBar.propTypes = {
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

    /** n_blur */
    n_blur: PropTypes.number,

    /** n_submit */
    n_submit: PropTypes.number,

    /** debounce */
    debounce: PropTypes.oneOfType([PropTypes.bool, PropTypes.number]),

    /**
     * helperText
     */
    helperText: PropTypes.any,

    /**
     * hideLabel
     */
    hideLabel: PropTypes.any,

    /**
     * label
     */
    label: PropTypes.any,

    /**
     * max
     */
    max: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

    /**
     * status
     */
    status: PropTypes.any,

    /**
     * type
     */
    type: PropTypes.any,

    /**
     * value
     */
    value: PropTypes.any,

};
