import React from 'react';
import { FluidComboBoxSkeleton as CarbonFluidComboBoxSkeleton } from '@carbon/react';

const FluidComboBoxSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFluidComboBoxSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFluidComboBoxSkeleton>
    );
};



export default FluidComboBoxSkeleton;
