import React from 'react';
import { TableActionList as CarbonTableActionList } from '@carbon/react';

const TableActionList = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTableActionList
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTableActionList>
    );
};



export default TableActionList;
