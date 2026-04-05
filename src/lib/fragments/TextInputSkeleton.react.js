import React from 'react';
import { TextInputSkeleton as CarbonTextInputSkeleton } from '@carbon/react';

const TextInputSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTextInputSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTextInputSkeleton>
    );
};



export default TextInputSkeleton;
