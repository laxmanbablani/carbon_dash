import React from 'react';
import { IconSwitch as CarbonIconSwitch } from '@carbon/react';

const IconSwitch = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonIconSwitch
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonIconSwitch>
    );
};



export default IconSwitch;
