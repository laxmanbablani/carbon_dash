import React from 'react';
import { GlobalTheme as CarbonGlobalTheme } from '@carbon/react';

const GlobalTheme = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonGlobalTheme
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonGlobalTheme>
    );
};



export default GlobalTheme;
