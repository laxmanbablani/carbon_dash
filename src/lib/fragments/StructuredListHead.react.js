import React from 'react';
import { StructuredListHead as CarbonStructuredListHead } from '@carbon/react';

const StructuredListHead = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonStructuredListHead
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonStructuredListHead>
    );
};



export default StructuredListHead;
