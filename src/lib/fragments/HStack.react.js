import React from 'react';
import { HStack as CarbonHStack } from '@carbon/react';

const HStack = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonHStack
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonHStack>
    );
};



export default HStack;
