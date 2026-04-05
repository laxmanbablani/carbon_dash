import React from 'react';
import { TableCell as CarbonTableCell } from '@carbon/react';

const TableCell = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTableCell
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTableCell>
    );
};



export default TableCell;
