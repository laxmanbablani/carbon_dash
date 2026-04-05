import React from 'react';
import { FluidTextInputSkeleton as CarbonFluidTextInputSkeleton } from '@carbon/react';

const FluidTextInputSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFluidTextInputSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFluidTextInputSkeleton>
    );
};



export default FluidTextInputSkeleton;
