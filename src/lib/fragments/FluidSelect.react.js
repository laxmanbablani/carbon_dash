import React from 'react';
import { FluidSelect as CarbonFluidSelect } from '@carbon/react';

const FluidSelect = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFluidSelect
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFluidSelect>
    );
};



export default FluidSelect;
