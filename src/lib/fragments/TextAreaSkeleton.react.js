import React from 'react';
import { TextAreaSkeleton as CarbonTextAreaSkeleton } from '@carbon/react';

const TextAreaSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTextAreaSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTextAreaSkeleton>
    );
};



export default TextAreaSkeleton;
