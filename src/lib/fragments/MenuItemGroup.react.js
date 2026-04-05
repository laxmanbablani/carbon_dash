import React from 'react';
import { MenuItemGroup as CarbonMenuItemGroup } from '@carbon/react';

const MenuItemGroup = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonMenuItemGroup
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonMenuItemGroup>
    );
};



export default MenuItemGroup;
