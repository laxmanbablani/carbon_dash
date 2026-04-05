import React from 'react';
import { TableBody as CarbonTableBody } from '@carbon/react';

const TableBody = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTableBody
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTableBody>
    );
};



export default TableBody;
