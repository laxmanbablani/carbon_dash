import React from 'react';
import { FluidDatePickerSkeleton as CarbonFluidDatePickerSkeleton } from '@carbon/react';

const FluidDatePickerSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFluidDatePickerSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFluidDatePickerSkeleton>
    );
};



export default FluidDatePickerSkeleton;
