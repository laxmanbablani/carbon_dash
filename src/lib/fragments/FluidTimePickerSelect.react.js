import React from 'react';
import { FluidTimePickerSelect as CarbonFluidTimePickerSelect } from '@carbon/react';

const FluidTimePickerSelect = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFluidTimePickerSelect
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFluidTimePickerSelect>
    );
};



export default FluidTimePickerSelect;
