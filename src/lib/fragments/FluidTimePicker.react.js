import React from 'react';
import { FluidTimePicker as CarbonFluidTimePicker } from '@carbon/react';

const FluidTimePicker = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFluidTimePicker
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFluidTimePicker>
    );
};



export default FluidTimePicker;
