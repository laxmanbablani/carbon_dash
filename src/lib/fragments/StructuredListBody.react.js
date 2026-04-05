import React from 'react';
import { StructuredListBody as CarbonStructuredListBody } from '@carbon/react';

const StructuredListBody = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonStructuredListBody
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonStructuredListBody>
    );
};



export default StructuredListBody;
