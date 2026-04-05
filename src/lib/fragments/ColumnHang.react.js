import React from 'react';
import { ColumnHang as CarbonColumnHang } from '@carbon/react';

const ColumnHang = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonColumnHang
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonColumnHang>
    );
};



export default ColumnHang;
