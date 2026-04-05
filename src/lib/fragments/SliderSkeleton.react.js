import React from 'react';
import { SliderSkeleton as CarbonSliderSkeleton } from '@carbon/react';

const SliderSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSliderSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSliderSkeleton>
    );
};



export default SliderSkeleton;
