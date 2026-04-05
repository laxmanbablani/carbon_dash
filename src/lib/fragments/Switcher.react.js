import React from 'react';
import { Switcher as CarbonSwitcher } from '@carbon/react';

const Switcher = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSwitcher
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSwitcher>
    );
};



export default Switcher;
