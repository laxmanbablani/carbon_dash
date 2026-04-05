import React from 'react';
import { PaginationSkeleton as CarbonPaginationSkeleton } from '@carbon/react';

const PaginationSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonPaginationSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonPaginationSkeleton>
    );
};



export default PaginationSkeleton;
