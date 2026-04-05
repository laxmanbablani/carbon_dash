import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * PasswordInput is a wrapper for the Carbon PasswordInput component.
 */
export default class PasswordInput extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['PasswordInput'];
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

PasswordInput.defaultProps = {
    className: '',
};

PasswordInput.propTypes = {
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
     * helperText
     */
    helperText: PropTypes.any,

    /**
     * hideLabel
     */
    hideLabel: PropTypes.any,

    /**
     * hidePasswordLabel
     */
    hidePasswordLabel: PropTypes.any,

    /**
     * inline
     */
    inline: PropTypes.any,

    /**
     * invalid
     */
    invalid: PropTypes.any,

    /**
     * readOnly
     */
    readOnly: PropTypes.any,

    /**
     * invalidText
     */
    invalidText: PropTypes.any,

    /**
     * labelText
     */
    labelText: PropTypes.any,

    /**
     * light
     */
    light: PropTypes.any,

    /**
     * onChange
     */
    onChange: PropTypes.any,

    /**
     * onClick
     */
    onClick: PropTypes.any,

    /**
     * onTogglePasswordVisibility
     */
    onTogglePasswordVisibility: PropTypes.any,

    /**
     * placeholder
     */
    placeholder: PropTypes.any,

    /**
     * showPasswordLabel
     */
    showPasswordLabel: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

    /**
     * tooltipAlignment
     */
    tooltipAlignment: PropTypes.any,

    /**
     * tooltipPosition
     */
    tooltipPosition: PropTypes.any,

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

};
