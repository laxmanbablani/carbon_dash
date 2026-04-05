import React from 'react';
import { AISkeletonPlaceholder as CarbonAISkeletonPlaceholder } from '@carbon/react';

const AISkeletonPlaceholder = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonAISkeletonPlaceholder
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonAISkeletonPlaceholder>
    );
};



export default AISkeletonPlaceholder;
