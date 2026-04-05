import React from 'react';
import { TableContainer as CarbonTableContainer } from '@carbon/react';

const TableContainer = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTableContainer
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTableContainer>
    );
};



export default TableContainer;
