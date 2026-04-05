import React from 'react';
import { DatePicker as CarbonDatePicker } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const DatePicker = (props) => {
    const {
        id,
        setProps,
        children,
        className = '',
        loading_state,
        style,
        datePickerType = 'single',
        value = '',
        ...otherProps
    } = props;
    return (
        <CarbonDatePicker
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            datePickerType={datePickerType}
            value={value}
            {...otherProps}
        >
            {children}
        </CarbonDatePicker>
    );
};

export default DatePicker;
