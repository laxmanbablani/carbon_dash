import React from 'react';
import { Theme as CarbonTheme } from '@carbon/react';

const Theme = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTheme
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTheme>
    );
};



export default Theme;
