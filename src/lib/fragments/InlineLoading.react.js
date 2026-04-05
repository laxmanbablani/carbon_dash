import React from 'react';
import { InlineLoading as CarbonInlineLoading } from '@carbon/react';

const InlineLoading = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonInlineLoading
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonInlineLoading>
    );
};



export default InlineLoading;
