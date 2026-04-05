import React from 'react';
import { TableSelectAll as CarbonTableSelectAll } from '@carbon/react';

const TableSelectAll = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTableSelectAll
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTableSelectAll>
    );
};



export default TableSelectAll;
