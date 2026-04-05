import React from 'react';
import { Switch as CarbonSwitch } from '@carbon/react';

const Switch = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSwitch
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSwitch>
    );
};



export default Switch;
