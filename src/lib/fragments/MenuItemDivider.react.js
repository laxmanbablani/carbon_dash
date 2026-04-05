import React from 'react';
import { MenuItemDivider as CarbonMenuItemDivider } from '@carbon/react';

const MenuItemDivider = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonMenuItemDivider
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonMenuItemDivider>
    );
};



export default MenuItemDivider;
