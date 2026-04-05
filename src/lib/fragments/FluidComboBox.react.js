import React from 'react';
import { FluidComboBox as CarbonFluidComboBox } from '@carbon/react';

const FluidComboBox = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFluidComboBox
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFluidComboBox>
    );
};



export default FluidComboBox;
