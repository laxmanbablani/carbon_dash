import React from 'react';
import { FormGroup as CarbonFormGroup } from '@carbon/react';

const FormGroup = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFormGroup
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFormGroup>
    );
};



export default FormGroup;
