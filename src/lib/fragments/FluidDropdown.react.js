import React from 'react';
import { FluidDropdown as CarbonFluidDropdown } from '@carbon/react';

const FluidDropdown = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFluidDropdown
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFluidDropdown>
    );
};



export default FluidDropdown;
