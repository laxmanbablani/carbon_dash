import React from 'react';
import { TableHead as CarbonTableHead } from '@carbon/react';

const TableHead = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTableHead
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTableHead>
    );
};



export default TableHead;
