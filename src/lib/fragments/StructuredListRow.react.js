import React from 'react';
import { StructuredListRow as CarbonStructuredListRow } from '@carbon/react';

const StructuredListRow = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonStructuredListRow
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonStructuredListRow>
    );
};



export default StructuredListRow;
