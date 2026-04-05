import React from 'react';
import { TableSelectRow as CarbonTableSelectRow } from '@carbon/react';

const TableSelectRow = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTableSelectRow
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTableSelectRow>
    );
};



export default TableSelectRow;
