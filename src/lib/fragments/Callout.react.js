import React from 'react';
import { Callout as CarbonCallout } from '@carbon/react';

const Callout = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonCallout
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonCallout>
    );
};



export default Callout;
