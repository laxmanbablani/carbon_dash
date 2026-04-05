import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Checkbox is a wrapper for the Carbon Checkbox component.
 */
export default class Checkbox extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { checked } = this.props;
        const { label } = this.props;

        const RealComponent = LazyLoader['Checkbox'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    checked={checked}
                    label={label}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

Checkbox.defaultProps = {
    className: '',
    checked: false,
    label: 'Checkbox',
};

Checkbox.propTypes = {
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
     * helperText
     */
    helperText: PropTypes.any,

    /**
     * hideLabel
     */
    hideLabel: PropTypes.any,

    /**
     * indeterminate
     */
    indeterminate: PropTypes.any,

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
     * onChange
     */
    onChange: PropTypes.any,

    /**
     * readOnly
     */
    readOnly: PropTypes.any,

    /**
     * slug
     */
    slug: PropTypes.any,

    /**
     * title
     */
    title: PropTypes.any,

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
