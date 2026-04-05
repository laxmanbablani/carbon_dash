import React from 'react';
import { SkeletonPlaceholder as CarbonSkeletonPlaceholder } from '@carbon/react';

const SkeletonPlaceholder = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSkeletonPlaceholder
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSkeletonPlaceholder>
    );
};



export default SkeletonPlaceholder;
