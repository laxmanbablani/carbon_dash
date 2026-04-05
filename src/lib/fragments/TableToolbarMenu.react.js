import React from 'react';
import { TableToolbarMenu as CarbonTableToolbarMenu } from '@carbon/react';

const TableToolbarMenu = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTableToolbarMenu
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTableToolbarMenu>
    );
};



export default TableToolbarMenu;
