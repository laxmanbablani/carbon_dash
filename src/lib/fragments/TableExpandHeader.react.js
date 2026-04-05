import React from 'react';
import { TableExpandHeader as CarbonTableExpandHeader } from '@carbon/react';

const TableExpandHeader = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTableExpandHeader
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTableExpandHeader>
    );
};



export default TableExpandHeader;
