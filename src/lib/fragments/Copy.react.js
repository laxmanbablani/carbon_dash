import React from 'react';
import { Copy as CarbonCopy } from '@carbon/react';

const Copy = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonCopy
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonCopy>
    );
};



export default Copy;
