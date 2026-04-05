import React from 'react';
import { BreadcrumbSkeleton as CarbonBreadcrumbSkeleton } from '@carbon/react';

const BreadcrumbSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonBreadcrumbSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonBreadcrumbSkeleton>
    );
};



export default BreadcrumbSkeleton;
