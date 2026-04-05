import React from 'react';
import { SkeletonText as CarbonSkeletonText } from '@carbon/react';

const SkeletonText = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSkeletonText
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSkeletonText>
    );
};



export default SkeletonText;
