import React from 'react';
import PropTypes from 'prop-types';
import { DatePickerInput as CarbonDatePickerInput } from '@carbon/react';

const DatePickerInput = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;
    return (
        <CarbonDatePickerInput
            id={id} className={className} style={style}
            data-dash-is-loading={loading_state?.is_loading || undefined}
            {...others}
        />
    );
};

DatePickerInput.propTypes = {
    id: PropTypes.string, children: PropTypes.node,
    className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    /** Label text */
    labelText: PropTypes.node,
    /** Placeholder text */
    placeholder: PropTypes.string,
    /** Helper text */
    helperText: PropTypes.node,
    /** Whether disabled */
    disabled: PropTypes.bool,
    /** Whether invalid */
    invalid: PropTypes.bool,
    /** Invalid text */
    invalidText: PropTypes.node,
    /** Input size */
    size: PropTypes.oneOf(['sm', 'md', 'lg']),
    /** Format pattern */
    pattern: PropTypes.string,
    /** DatePickerInput type */
    type: PropTypes.string,
};

DatePickerInput.defaultProps = { disabled: false, size: 'md' };

export default DatePickerInput;
