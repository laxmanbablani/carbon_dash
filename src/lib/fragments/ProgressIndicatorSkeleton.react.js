import React from 'react';
import { ProgressIndicatorSkeleton as CarbonProgressIndicatorSkeleton } from '@carbon/react';

const ProgressIndicatorSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonProgressIndicatorSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonProgressIndicatorSkeleton>
    );
};



export default ProgressIndicatorSkeleton;
