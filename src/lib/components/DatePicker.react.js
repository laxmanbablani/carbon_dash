import React from 'react';
import PropTypes from 'prop-types';
import {
    DatePicker as CarbonDatePicker,
    DatePickerSkeleton as CarbonDatePickerSkeleton,
} from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const DatePicker = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;

    if (loading_state && loading_state.is_loading) {
        return <CarbonDatePickerSkeleton id={id} className={className} />;
    }

    return (
        <CarbonDatePicker
            id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonDatePicker>
    );
};

DatePicker.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func,
    children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    /** Date picker type: 'single' or 'range' */
    datePickerType: PropTypes.oneOf(['single', 'range']),
    /** The current date value(s). For single: string. For range: [start, end] */
    value: PropTypes.oneOfType([PropTypes.string, PropTypes.arrayOf(PropTypes.string)]),
    /** Format pattern for dates */
    dateFormat: PropTypes.string,
    /** Default value */
    defaultValue: PropTypes.oneOfType([PropTypes.string, PropTypes.arrayOf(PropTypes.string)]),
    /** Whether disabled */
    disabled: PropTypes.bool,
    /** Whether readonly */
    readOnly: PropTypes.bool,
    /** Light variant */
    light: PropTypes.bool,
    /** Short style without calendar */
    short: PropTypes.bool,
    /** Minimum date */
    minDate: PropTypes.string,
    /** Maximum date */
    maxDate: PropTypes.string,
    /** Locale for formatting */
    locale: PropTypes.string,
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

DatePicker.defaultProps = { datePickerType: 'single', disabled: false, readOnly: false, short: false, light: false };

export default DatePicker;
