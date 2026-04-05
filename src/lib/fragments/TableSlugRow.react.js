import React from 'react';
import { TableSlugRow as CarbonTableSlugRow } from '@carbon/react';

const TableSlugRow = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTableSlugRow
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTableSlugRow>
    );
};



export default TableSlugRow;
