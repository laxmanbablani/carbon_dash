import React from 'react';
import { Form as CarbonForm } from '@carbon/react';

const Form = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonForm
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonForm>
    );
};



export default Form;
