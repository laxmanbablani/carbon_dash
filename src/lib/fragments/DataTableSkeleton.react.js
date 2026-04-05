import React from 'react';
import { DataTableSkeleton as CarbonDataTableSkeleton } from '@carbon/react';

const DataTableSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonDataTableSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonDataTableSkeleton>
    );
};



export default DataTableSkeleton;
