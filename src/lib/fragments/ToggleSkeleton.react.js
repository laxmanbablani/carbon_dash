import React from 'react';
import { ToggleSkeleton as CarbonToggleSkeleton } from '@carbon/react';

const ToggleSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonToggleSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonToggleSkeleton>
    );
};



export default ToggleSkeleton;
