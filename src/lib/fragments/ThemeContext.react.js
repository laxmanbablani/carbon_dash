import React from 'react';
import { ThemeContext as CarbonThemeContext } from '@carbon/react';

const ThemeContext = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonThemeContext
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonThemeContext>
    );
};



export default ThemeContext;
