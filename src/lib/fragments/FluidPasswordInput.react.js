import React from 'react';
import { FluidPasswordInput as CarbonFluidPasswordInput } from '@carbon/react';

const FluidPasswordInput = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFluidPasswordInput
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFluidPasswordInput>
    );
};



export default FluidPasswordInput;
