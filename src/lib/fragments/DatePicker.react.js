import React from 'react';
import { DatePicker as CarbonDatePicker, DatePickerInput } from '@carbon/react';

const DatePicker = (props) => {
    const {
        id,
        setProps,
        children,
        className = '',
        style,
        datePickerType,
        ...otherProps
    } = props;

    // If no children provided, we render a default DatePickerInput
    const content = children || (
        <DatePickerInput
            id={`${id}-input`}
            labelText="Select date"
            placeholder="mm/dd/yyyy"
            size="md"
        />
    );

    return (
        <CarbonDatePicker
            id={id}
            className={className}
            style={style}
            datePickerType={datePickerType}
            {...otherProps}
        >
            {content}
        </CarbonDatePicker>
    );
};

export default DatePicker;
