import React from 'react';
import { FluidTimePickerSkeleton as CarbonFluidTimePickerSkeleton } from '@carbon/react';

const FluidTimePickerSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFluidTimePickerSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFluidTimePickerSkeleton>
    );
};



export default FluidTimePickerSkeleton;
