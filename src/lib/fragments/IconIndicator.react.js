import React from 'react';
import { IconIndicator as CarbonIconIndicator } from '@carbon/react';

const IconIndicator = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonIconIndicator
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonIconIndicator>
    );
};



export default IconIndicator;
