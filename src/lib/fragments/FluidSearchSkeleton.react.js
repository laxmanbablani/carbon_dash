import React from 'react';
import { FluidSearchSkeleton as CarbonFluidSearchSkeleton } from '@carbon/react';

const FluidSearchSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFluidSearchSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFluidSearchSkeleton>
    );
};



export default FluidSearchSkeleton;
