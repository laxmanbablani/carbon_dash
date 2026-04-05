import React from 'react';
import { NumberInputSkeleton as CarbonNumberInputSkeleton } from '@carbon/react';

const NumberInputSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonNumberInputSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonNumberInputSkeleton>
    );
};



export default NumberInputSkeleton;
