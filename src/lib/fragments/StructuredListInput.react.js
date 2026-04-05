import React from 'react';
import { StructuredListInput as CarbonStructuredListInput } from '@carbon/react';

const StructuredListInput = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonStructuredListInput
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonStructuredListInput>
    );
};



export default StructuredListInput;
