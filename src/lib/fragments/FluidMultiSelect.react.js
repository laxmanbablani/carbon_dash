import React from 'react';
import { FluidMultiSelect as CarbonFluidMultiSelect } from '@carbon/react';

const FluidMultiSelect = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFluidMultiSelect
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFluidMultiSelect>
    );
};



export default FluidMultiSelect;
