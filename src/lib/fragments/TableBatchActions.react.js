import React from 'react';
import { TableBatchActions as CarbonTableBatchActions } from '@carbon/react';

const TableBatchActions = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTableBatchActions
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTableBatchActions>
    );
};



export default TableBatchActions;
