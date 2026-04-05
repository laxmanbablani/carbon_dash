import React from 'react';
import { TableHeader as CarbonTableHeader } from '@carbon/react';

const TableHeader = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTableHeader
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTableHeader>
    );
};



export default TableHeader;
