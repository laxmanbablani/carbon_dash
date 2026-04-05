import React from 'react';
import { IconTab as CarbonIconTab } from '@carbon/react';

const IconTab = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonIconTab
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonIconTab>
    );
};



export default IconTab;
