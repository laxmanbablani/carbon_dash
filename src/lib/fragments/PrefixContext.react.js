import React from 'react';
import { PrefixContext as CarbonPrefixContext } from '@carbon/react';

const PrefixContext = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonPrefixContext
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonPrefixContext>
    );
};



export default PrefixContext;
