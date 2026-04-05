import React from 'react';
import { TableToolbarAction as CarbonTableToolbarAction } from '@carbon/react';

const TableToolbarAction = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTableToolbarAction
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTableToolbarAction>
    );
};



export default TableToolbarAction;
