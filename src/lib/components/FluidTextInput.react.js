import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * FluidTextInput is a wrapper for the Carbon FluidTextInput component.
 */
export default class FluidTextInput extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['FluidTextInput'];
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

FluidTextInput.defaultProps = {
    className: '',
};

FluidTextInput.propTypes = {
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
     * defaultValue
     */
    defaultValue: PropTypes.any,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * invalid
     */
    invalid: PropTypes.any,

    /**
     * invalidText
     */
    invalidText: PropTypes.any,

    /**
     * isPassword
     */
    isPassword: PropTypes.any,

    /**
     * maxCount
     */
    maxCount: PropTypes.any,

    /**
     * enableCounter
     */
    enableCounter: PropTypes.any,

    /**
     * labelText
     */
    labelText: PropTypes.any,

    /**
     * onChange
     */
    onChange: PropTypes.any,

    /**
     * onClick
     */
    onClick: PropTypes.any,

    /**
     * placeholder
     */
    placeholder: PropTypes.any,

    /**
     * value
     */
    value: PropTypes.any,

    /**
     * warn
     */
    warn: PropTypes.any,

    /**
     * warnText
     */
    warnText: PropTypes.any,

    /**
     * readOnly
     */
    readOnly: PropTypes.any,

};
