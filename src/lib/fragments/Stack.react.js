import React from 'react';
import { Stack as CarbonStack } from '@carbon/react';

const Stack = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonStack
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonStack>
    );
};



export default Stack;
