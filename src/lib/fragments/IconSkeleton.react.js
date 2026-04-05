import React from 'react';
import { IconSkeleton as CarbonIconSkeleton } from '@carbon/react';

const IconSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonIconSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonIconSkeleton>
    );
};



export default IconSkeleton;
