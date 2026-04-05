import React from 'react';
import { AISkeletonIcon as CarbonAISkeletonIcon } from '@carbon/react';

const AISkeletonIcon = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonAISkeletonIcon
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonAISkeletonIcon>
    );
};



export default AISkeletonIcon;
