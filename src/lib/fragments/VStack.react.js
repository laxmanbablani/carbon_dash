import React from 'react';
import { VStack as CarbonVStack } from '@carbon/react';

const VStack = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonVStack
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonVStack>
    );
};



export default VStack;
