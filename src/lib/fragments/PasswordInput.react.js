import React from 'react';
import { PasswordInput as CarbonPasswordInput } from '@carbon/react';

const PasswordInput = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonPasswordInput
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonPasswordInput>
    );
};



export default PasswordInput;
