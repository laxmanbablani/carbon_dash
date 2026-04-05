import React from 'react';
import { StructuredListCell as CarbonStructuredListCell } from '@carbon/react';

const StructuredListCell = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonStructuredListCell
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonStructuredListCell>
    );
};



export default StructuredListCell;
