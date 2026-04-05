import React from 'react';
import { StructuredListWrapper as CarbonStructuredListWrapper } from '@carbon/react';

const StructuredListWrapper = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonStructuredListWrapper
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonStructuredListWrapper>
    );
};



export default StructuredListWrapper;
