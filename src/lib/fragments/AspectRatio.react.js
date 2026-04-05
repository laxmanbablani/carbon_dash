import React from 'react';
import { AspectRatio as CarbonAspectRatio } from '@carbon/react';

const AspectRatio = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonAspectRatio
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonAspectRatio>
    );
};



export default AspectRatio;
