import React from 'react';
import { FluidDatePickerInput as CarbonFluidDatePickerInput } from '@carbon/react';

const FluidDatePickerInput = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFluidDatePickerInput
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFluidDatePickerInput>
    );
};



export default FluidDatePickerInput;
