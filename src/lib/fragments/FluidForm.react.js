import React from 'react';
import { FluidForm as CarbonFluidForm } from '@carbon/react';

const FluidForm = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFluidForm
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFluidForm>
    );
};



export default FluidForm;
