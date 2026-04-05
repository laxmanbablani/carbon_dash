import React from 'react';
import { FluidTextArea as CarbonFluidTextArea } from '@carbon/react';

const FluidTextArea = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFluidTextArea
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFluidTextArea>
    );
};



export default FluidTextArea;
