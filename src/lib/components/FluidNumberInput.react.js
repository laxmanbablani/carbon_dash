import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * FluidNumberInput is a wrapper for the Carbon FluidNumberInput component.
 */
export default class FluidNumberInput extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['FluidNumberInput'];
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

FluidNumberInput.defaultProps = {
    className: '',
};

FluidNumberInput.propTypes = {
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
    label: PropTypes.any,

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
