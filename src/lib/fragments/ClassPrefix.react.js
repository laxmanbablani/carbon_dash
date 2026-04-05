import React from 'react';
import { ClassPrefix as CarbonClassPrefix } from '@carbon/react';

const ClassPrefix = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonClassPrefix
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonClassPrefix>
    );
};



export default ClassPrefix;
