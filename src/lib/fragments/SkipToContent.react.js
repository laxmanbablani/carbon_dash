import React from 'react';
import { SkipToContent as CarbonSkipToContent } from '@carbon/react';

const SkipToContent = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSkipToContent
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSkipToContent>
    );
};



export default SkipToContent;
