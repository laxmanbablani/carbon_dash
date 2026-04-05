import React from 'react';
import { FluidDropdownSkeleton as CarbonFluidDropdownSkeleton } from '@carbon/react';

const FluidDropdownSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFluidDropdownSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFluidDropdownSkeleton>
    );
};



export default FluidDropdownSkeleton;
