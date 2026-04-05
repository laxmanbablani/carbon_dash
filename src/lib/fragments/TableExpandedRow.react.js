import React from 'react';
import { TableExpandedRow as CarbonTableExpandedRow } from '@carbon/react';

const TableExpandedRow = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTableExpandedRow
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTableExpandedRow>
    );
};



export default TableExpandedRow;
