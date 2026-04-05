import React from 'react';
import { DropdownSkeleton as CarbonDropdownSkeleton } from '@carbon/react';

const DropdownSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonDropdownSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonDropdownSkeleton>
    );
};



export default DropdownSkeleton;
