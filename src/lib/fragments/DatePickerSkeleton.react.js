import React from 'react';
import { DatePickerSkeleton as CarbonDatePickerSkeleton } from '@carbon/react';

const DatePickerSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonDatePickerSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonDatePickerSkeleton>
    );
};



export default DatePickerSkeleton;
