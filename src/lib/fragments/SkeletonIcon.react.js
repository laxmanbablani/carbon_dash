import React from 'react';
import { SkeletonIcon as CarbonSkeletonIcon } from '@carbon/react';

const SkeletonIcon = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSkeletonIcon
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSkeletonIcon>
    );
};



export default SkeletonIcon;
