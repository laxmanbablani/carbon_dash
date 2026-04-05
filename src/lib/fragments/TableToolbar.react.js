import React from 'react';
import { TableToolbar as CarbonTableToolbar } from '@carbon/react';

const TableToolbar = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTableToolbar
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTableToolbar>
    );
};



export default TableToolbar;
