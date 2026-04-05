import React from 'react';
import { TableRow as CarbonTableRow } from '@carbon/react';

const TableRow = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTableRow
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTableRow>
    );
};



export default TableRow;
