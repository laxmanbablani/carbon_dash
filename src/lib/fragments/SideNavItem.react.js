import React from 'react';
import { SideNavItem as CarbonSideNavItem } from '@carbon/react';

const SideNavItem = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSideNavItem
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSideNavItem>
    );
};



export default SideNavItem;
