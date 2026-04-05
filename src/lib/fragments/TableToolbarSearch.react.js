import React from 'react';
import { TableToolbarSearch as CarbonTableToolbarSearch } from '@carbon/react';

const TableToolbarSearch = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTableToolbarSearch
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTableToolbarSearch>
    );
};



export default TableToolbarSearch;
