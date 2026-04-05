import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * RadioButton is a wrapper for the Carbon RadioButton component.
 */
export default class RadioButton extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { checked } = this.props;
        const { label } = this.props;
        const { value } = this.props;

        const RealComponent = LazyLoader['RadioButton'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    checked={checked}
                    label={label}
                    value={value}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

RadioButton.defaultProps = {
    className: '',
    checked: false,
    label: 'Radio Button',
    value: '',
};

RadioButton.propTypes = {
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
     * checked
     */
    checked: PropTypes.bool,

    /**
     * decorator
     */
    decorator: PropTypes.any,

    /**
     * defaultChecked
     */
    defaultChecked: PropTypes.any,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * hideLabel
     */
    hideLabel: PropTypes.any,

    /**
     * labelPosition
     */
    labelPosition: PropTypes.any,

    /**
     * labelText
     */
    labelText: PropTypes.any,

    /**
     * name
     */
    name: PropTypes.any,

    /**
     * onChange
     */
    onChange: PropTypes.any,

    /**
     * onClick
     */
    onClick: PropTypes.any,

    /**
     * required
     */
    required: PropTypes.any,

    /**
     * invalid
     */
    invalid: PropTypes.any,

    /**
     * invalidText
     */
    invalidText: PropTypes.any,

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

    /**
     * slug
     */
    slug: PropTypes.any,

    /**
     * value
     */
    value: PropTypes.any,

    /**
     * label
     */
    label: PropTypes.string,

};
