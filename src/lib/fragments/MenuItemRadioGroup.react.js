import React from 'react';
import { MenuItemRadioGroup as CarbonMenuItemRadioGroup } from '@carbon/react';

const MenuItemRadioGroup = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonMenuItemRadioGroup
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonMenuItemRadioGroup>
    );
};



export default MenuItemRadioGroup;
