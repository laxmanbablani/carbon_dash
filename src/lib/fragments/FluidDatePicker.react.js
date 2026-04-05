import React from 'react';
import { FluidDatePicker as CarbonFluidDatePicker } from '@carbon/react';

const FluidDatePicker = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFluidDatePicker
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFluidDatePicker>
    );
};



export default FluidDatePicker;
