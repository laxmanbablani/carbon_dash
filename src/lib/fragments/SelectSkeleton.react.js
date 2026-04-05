import React from 'react';
import { SelectSkeleton as CarbonSelectSkeleton } from '@carbon/react';

const SelectSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSelectSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSelectSkeleton>
    );
};



export default SelectSkeleton;
