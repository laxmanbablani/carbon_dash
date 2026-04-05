import React from 'react';
import { RadioButtonSkeleton as CarbonRadioButtonSkeleton } from '@carbon/react';

const RadioButtonSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonRadioButtonSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonRadioButtonSkeleton>
    );
};



export default RadioButtonSkeleton;
