import React from 'react';
import { ControlledPasswordInput as CarbonControlledPasswordInput } from '@carbon/react';

const ControlledPasswordInput = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonControlledPasswordInput
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonControlledPasswordInput>
    );
};



export default ControlledPasswordInput;
