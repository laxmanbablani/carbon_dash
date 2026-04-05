import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Select is a wrapper for the Carbon Select component.
 */
export default class Select extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { value } = this.props;
        const { label } = this.props;

        const RealComponent = LazyLoader['Select'];
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

Select.defaultProps = {
    className: '',
    value: '',
    label: 'Select',
};

Select.propTypes = {
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

    /**
     * decorator
     */
    decorator: PropTypes.any,

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
     * inline
     */
    inline: PropTypes.any,

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
     * light
     */
    light: PropTypes.any,

    /**
     * noLabel
     */
    noLabel: PropTypes.any,

    /**
     * onChange
     */
    onChange: PropTypes.any,

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
     * warn
     */
    warn: PropTypes.any,

    /**
     * warnText
     */
    warnText: PropTypes.any,

    /**
     * value
     */
    value: PropTypes.any,

    /**
     * label
     */
    label: PropTypes.string,

};
