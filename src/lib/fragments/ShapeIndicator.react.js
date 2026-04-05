import React from 'react';
import { ShapeIndicator as CarbonShapeIndicator } from '@carbon/react';

const ShapeIndicator = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonShapeIndicator
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonShapeIndicator>
    );
};



export default ShapeIndicator;
