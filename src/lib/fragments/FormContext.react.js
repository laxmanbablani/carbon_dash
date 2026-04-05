import React from 'react';
import { FormContext as CarbonFormContext } from '@carbon/react';

const FormContext = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFormContext
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFormContext>
    );
};



export default FormContext;
