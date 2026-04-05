import React from 'react';
import { SideNavMenuItem as CarbonSideNavMenuItem } from '@carbon/react';

const SideNavMenuItem = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSideNavMenuItem
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSideNavMenuItem>
    );
};



export default SideNavMenuItem;
