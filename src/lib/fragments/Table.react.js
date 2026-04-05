import React from 'react';
import { Table as CarbonTable } from '@carbon/react';

const Table = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTable
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTable>
    );
};



export default Table;
