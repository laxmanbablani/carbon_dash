import React from 'react';
import { TableToolbarContent as CarbonTableToolbarContent } from '@carbon/react';

const TableToolbarContent = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTableToolbarContent
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTableToolbarContent>
    );
};



export default TableToolbarContent;
