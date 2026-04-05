import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Slider is a wrapper for the Carbon Slider component.
 */
export default class Slider extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { value } = this.props;
        const { min } = this.props;
        const { max } = this.props;
        const { label } = this.props;

        const RealComponent = LazyLoader['Slider'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    value={value}
                    min={min}
                    max={max}
                    label={label}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

Slider.defaultProps = {
    className: '',
    value: 0,
    min: 0,
    max: 100,
    label: 'Slider',
};

Slider.propTypes = {
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
     * ariaLabelInput
     */
    ariaLabelInput: PropTypes.any,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * formatLabel
     */
    formatLabel: PropTypes.any,

    /**
     * hideTextInput
     */
    hideTextInput: PropTypes.any,

    /**
     * inputType
     */
    inputType: PropTypes.any,

    /**
     * invalid
     */
    invalid: PropTypes.any,

    /**
     * invalidText
     */
    invalidText: PropTypes.any,

    /**
     * labelText
     */
    labelText: PropTypes.any,

    /**
     * hideLabel
     */
    hideLabel: PropTypes.any,

    /**
     * light
     */
    light: PropTypes.any,

    /**
     * max
     */
    max: PropTypes.number,

    /**
     * maxLabel
     */
    maxLabel: PropTypes.any,

    /**
     * min
     */
    min: PropTypes.number,

    /**
     * minLabel
     */
    minLabel: PropTypes.any,

    /**
     * name
     */
    name: PropTypes.any,

    /**
     * onBlur
     */
    onBlur: PropTypes.any,

    /**
     * onChange
     */
    onChange: PropTypes.any,

    /**
     * onInputKeyUp
     */
    onInputKeyUp: PropTypes.any,

    /**
     * onRelease
     */
    onRelease: PropTypes.any,

    /**
     * readOnly
     */
    readOnly: PropTypes.any,

    /**
     * required
     */
    required: PropTypes.any,

    /**
     * step
     */
    step: PropTypes.any,

    /**
     * stepMultiplier
     */
    stepMultiplier: PropTypes.any,

    /**
     * translateWithId
     */
    translateWithId: PropTypes.any,

    /**
     * unstable_ariaLabelInputUpper
     */
    unstable_ariaLabelInputUpper: PropTypes.any,

    /**
     * unstable_nameUpper
     */
    unstable_nameUpper: PropTypes.any,

    /**
     * unstable_valueUpper
     */
    unstable_valueUpper: PropTypes.any,

    /**
     * value
     */
    value: PropTypes.number,

    /**
     * warn
     */
    warn: PropTypes.any,

    /**
     * warnText
     */
    warnText: PropTypes.any,

    /**
     * label
     */
    label: PropTypes.string,

};
