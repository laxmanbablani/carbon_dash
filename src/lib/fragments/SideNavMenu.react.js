import React from 'react';
import { SideNavMenu as CarbonSideNavMenu } from '@carbon/react';

const SideNavMenu = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSideNavMenu
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSideNavMenu>
    );
};



export default SideNavMenu;
