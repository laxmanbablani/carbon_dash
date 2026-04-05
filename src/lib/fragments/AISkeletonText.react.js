import React from 'react';
import { AISkeletonText as CarbonAISkeletonText } from '@carbon/react';

const AISkeletonText = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonAISkeletonText
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonAISkeletonText>
    );
};



export default AISkeletonText;
