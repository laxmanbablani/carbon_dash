import React from 'react';
import { TableExpandRow as CarbonTableExpandRow } from '@carbon/react';

const TableExpandRow = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTableExpandRow
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTableExpandRow>
    );
};



export default TableExpandRow;
