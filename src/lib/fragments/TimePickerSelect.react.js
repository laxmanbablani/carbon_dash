import React from 'react';
import { TimePickerSelect as CarbonTimePickerSelect } from '@carbon/react';

const TimePickerSelect = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTimePickerSelect
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTimePickerSelect>
    );
};



export default TimePickerSelect;
