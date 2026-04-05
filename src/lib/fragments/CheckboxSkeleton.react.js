import React from 'react';
import { CheckboxSkeleton as CarbonCheckboxSkeleton } from '@carbon/react';

const CheckboxSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonCheckboxSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonCheckboxSkeleton>
    );
};



export default CheckboxSkeleton;
