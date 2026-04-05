import React from 'react';
import { TagSkeleton as CarbonTagSkeleton } from '@carbon/react';

const TagSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTagSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTagSkeleton>
    );
};



export default TagSkeleton;
