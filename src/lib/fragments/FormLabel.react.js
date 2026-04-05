import React from 'react';
import { FormLabel as CarbonFormLabel } from '@carbon/react';

const FormLabel = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFormLabel
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFormLabel>
    );
};



export default FormLabel;
