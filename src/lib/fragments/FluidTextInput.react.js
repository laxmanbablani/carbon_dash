import React from 'react';
import { FluidTextInput as CarbonFluidTextInput } from '@carbon/react';

const FluidTextInput = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFluidTextInput
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFluidTextInput>
    );
};



export default FluidTextInput;
