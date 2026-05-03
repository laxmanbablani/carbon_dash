import React from 'react';
import PropTypes from 'prop-types';
import { DatePickerInput as CarbonDatePickerInput } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * FluidDatePickerInput is a full-width date picker input component.
 */
const FluidDatePickerInput = (props) => {
    const {
        id,
        children,
        className = '',
        style = {},
        loading_state,
        placeholder = 'mm/dd/yyyy',
        labelText,
        dateFormat = 'm/d/Y',
        pattern = '\\d{1,2}/\\d{1,2}/\\d{4}',
        ...others
    } = props;

    return (
        <CarbonDatePickerInput
            id={id}
            className={className}
            style={style}
            placeholder={placeholder}
            labelText={labelText}
            dateFormat={dateFormat}
            pattern={pattern}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonDatePickerInput>
    );
};

FluidDatePickerInput.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

    /** Dash callback to update props */
    setProps: PropTypes.func,

    /** The content of the date picker input */
    children: PropTypes.node,

    /** Custom CSS class */
    className: PropTypes.string,

    /** Inline styles */
    style: PropTypes.object,

    /** Dash loading state */
    loading_state: PropTypes.shape({
        is_loading: PropTypes.bool,
        prop_name: PropTypes.string,
        component_name: PropTypes.string,
    }),

    /** Provide the placeholder text for the date picker input */
    placeholder: PropTypes.string,

    /** Provide the label text for the date picker input */
    labelText: PropTypes.node,

    /** Specify the date format */
    dateFormat: PropTypes.string,

    /** Specify the pattern for the date input */
    pattern: PropTypes.string,

    /** Specify whether the control is disabled */
    disabled: PropTypes.bool,

    /** Persistence settings */
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

FluidDatePickerInput.defaultProps = {
    placeholder: 'mm/dd/yyyy',
    dateFormat: 'm/d/Y',
    pattern: '\\d{1,2}/\\d{1,2}/\\d{4}',
    disabled: false,
};

export default FluidDatePickerInput;