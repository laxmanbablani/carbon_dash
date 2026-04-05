import React from 'react';
import { SideNavIcon as CarbonSideNavIcon } from '@carbon/react';

const SideNavIcon = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSideNavIcon
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSideNavIcon>
    );
};



export default SideNavIcon;
