import React from 'react';
import { StructuredListSkeleton as CarbonStructuredListSkeleton } from '@carbon/react';

const StructuredListSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonStructuredListSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonStructuredListSkeleton>
    );
};



export default StructuredListSkeleton;
