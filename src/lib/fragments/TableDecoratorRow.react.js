import React from 'react';
import { TableDecoratorRow as CarbonTableDecoratorRow } from '@carbon/react';

const TableDecoratorRow = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTableDecoratorRow
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTableDecoratorRow>
    );
};



export default TableDecoratorRow;
