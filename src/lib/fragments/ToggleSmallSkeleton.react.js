import React from 'react';
import { ToggleSmallSkeleton as CarbonToggleSmallSkeleton } from '@carbon/react';

const ToggleSmallSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonToggleSmallSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonToggleSmallSkeleton>
    );
};



export default ToggleSmallSkeleton;
