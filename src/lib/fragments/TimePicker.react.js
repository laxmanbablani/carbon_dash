import React from 'react';
import { TimePicker as CarbonTimePicker } from '@carbon/react';

const TimePicker = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTimePicker
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTimePicker>
    );
};



export default TimePicker;
