import React from 'react';
import { FluidMultiSelectSkeleton as CarbonFluidMultiSelectSkeleton } from '@carbon/react';

const FluidMultiSelectSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFluidMultiSelectSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFluidMultiSelectSkeleton>
    );
};



export default FluidMultiSelectSkeleton;
