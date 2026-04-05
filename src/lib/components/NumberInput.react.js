import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * NumberInput is a wrapper for the Carbon NumberInput component.
 */
export default class NumberInput extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { value } = this.props;
        const { label } = this.props;

        const RealComponent = LazyLoader['NumberInput'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    value={value}
                    label={label}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

NumberInput.defaultProps = {
    className: '',
    value: 0,
    label: 'Number Input',
};

NumberInput.propTypes = {
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
     * allowEmpty
     */
    allowEmpty: PropTypes.any,

    /**
     * decorator
     */
    decorator: PropTypes.any,

    /**
     * defaultValue
     */
    defaultValue: PropTypes.any,

    /**
     * disableWheel
     */
    disableWheel: PropTypes.any,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * formatOptions
     */
    formatOptions: PropTypes.any,

    /**
     * helperText
     */
    helperText: PropTypes.any,

    /**
     * hideLabel
     */
    hideLabel: PropTypes.any,

    /**
     * hideSteppers
     */
    hideSteppers: PropTypes.any,

    /**
     * iconDescription
     */
    iconDescription: PropTypes.any,

    /**
     * inputMode
     */
    inputMode: PropTypes.any,

    /**
     * invalid
     */
    invalid: PropTypes.any,

    /**
     * invalidText
     */
    invalidText: PropTypes.any,

    /**
     * label
     */
    label: PropTypes.string,

    /**
     * light
     */
    light: PropTypes.any,

    /**
     * locale
     */
    locale: PropTypes.any,

    /**
     * max
     */
    max: PropTypes.any,

    /**
     * min
     */
    min: PropTypes.any,

    /**
     * stepStartValue
     */
    stepStartValue: PropTypes.any,

    /**
     * onBlur
     */
    onBlur: PropTypes.any,

    /**
     * onStepperBlur
     */
    onStepperBlur: PropTypes.any,

    /**
     * onChange
     */
    onChange: PropTypes.any,

    /**
     * onClick
     */
    onClick: PropTypes.any,

    /**
     * onKeyUp
     */
    onKeyUp: PropTypes.any,

    /**
     * pattern
     */
    pattern: PropTypes.any,

    /**
     * readOnly
     */
    readOnly: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

    /**
     * slug
     */
    slug: PropTypes.any,

    /**
     * step
     */
    step: PropTypes.any,

    /**
     * translateWithId
     */
    translateWithId: PropTypes.any,

    /**
     * type
     */
    type: PropTypes.any,

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
     * validate
     */
    validate: PropTypes.any,

};
