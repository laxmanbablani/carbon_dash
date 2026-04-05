import React from 'react';
import { DatePickerInput as CarbonDatePickerInput } from '@carbon/react';

const DatePickerInput = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonDatePickerInput
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonDatePickerInput>
    );
};



export default DatePickerInput;
