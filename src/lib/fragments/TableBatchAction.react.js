import React from 'react';
import { TableBatchAction as CarbonTableBatchAction } from '@carbon/react';

const TableBatchAction = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTableBatchAction
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTableBatchAction>
    );
};



export default TableBatchAction;
