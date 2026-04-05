import React from 'react';
import { FluidTextAreaSkeleton as CarbonFluidTextAreaSkeleton } from '@carbon/react';

const FluidTextAreaSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFluidTextAreaSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFluidTextAreaSkeleton>
    );
};



export default FluidTextAreaSkeleton;
