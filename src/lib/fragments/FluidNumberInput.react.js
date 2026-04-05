import React from 'react';
import { FluidNumberInput as CarbonFluidNumberInput } from '@carbon/react';

const FluidNumberInput = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFluidNumberInput
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFluidNumberInput>
    );
};



export default FluidNumberInput;
