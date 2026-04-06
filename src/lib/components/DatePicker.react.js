import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * DatePicker is a wrapper for the Carbon DatePicker component.
 */
export default class DatePicker extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { datePickerType } = this.props;
        const { value } = this.props;

        const RealComponent = LazyLoader['DatePicker'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    datePickerType={datePickerType}
                    value={value}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

DatePicker.defaultProps = {
    className: '',
    datePickerType: 'single',
    value: '',
};

DatePicker.propTypes = {
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
     * allowInput
     */
    allowInput: PropTypes.any,

    /**
     * appendTo
     */
    appendTo: PropTypes.any,

    /**
     * closeOnSelect
     */
    closeOnSelect: PropTypes.any,

    /**
     * dateFormat
     */
    dateFormat: PropTypes.any,

    /**
     * datePickerType
     */
    datePickerType: PropTypes.string,

    /**
     * disable
     */
    disable: PropTypes.any,

    /**
     * enable
     */
    enable: PropTypes.any,

    /**
     * inline
     */
    inline: PropTypes.any,

    /**
     * invalid
     */
    invalid: PropTypes.any,

    /**
     * light
     */
    light: PropTypes.any,

    /**
     * maxDate
     */
    maxDate: PropTypes.any,

    /**
     * minDate
     */
    minDate: PropTypes.any,

    /**
     * onChange
     */
    onChange: PropTypes.any,

    /**
     * onClose
     */
    onClose: PropTypes.any,

    /**
     * onOpen
     */
    onOpen: PropTypes.any,

    /**
     * parseDate
     */
    parseDate: PropTypes.any,

    /**
     * readOnly
     */
    readOnly: PropTypes.any,

    /**
     * short
     */
    short: PropTypes.any,

    /**
     * value
     */
    value: PropTypes.any,

    /**
     * warn
     */
    warn: PropTypes.any,

    /**
     * nextMonthAriaLabel
     */
    nextMonthAriaLabel: PropTypes.any,

    /**
     * prevMonthAriaLabel
     */
    prevMonthAriaLabel: PropTypes.any,

    /**
     * locale
     */
    locale: PropTypes.any,

    /**
     * invalidText
     */
    invalidText: PropTypes.any,

    /**
     * warnText
     */
    warnText: PropTypes.any,

};
