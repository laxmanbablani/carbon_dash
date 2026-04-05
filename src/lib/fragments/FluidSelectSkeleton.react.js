import React from 'react';
import { FluidSelectSkeleton as CarbonFluidSelectSkeleton } from '@carbon/react';

const FluidSelectSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFluidSelectSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFluidSelectSkeleton>
    );
};



export default FluidSelectSkeleton;
