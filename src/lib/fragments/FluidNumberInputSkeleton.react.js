import React from 'react';
import { FluidNumberInputSkeleton as CarbonFluidNumberInputSkeleton } from '@carbon/react';

const FluidNumberInputSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFluidNumberInputSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFluidNumberInputSkeleton>
    );
};



export default FluidNumberInputSkeleton;
