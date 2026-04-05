import React from 'react';
import { MenuItemSelectable as CarbonMenuItemSelectable } from '@carbon/react';

const MenuItemSelectable = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonMenuItemSelectable
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonMenuItemSelectable>
    );
};



export default MenuItemSelectable;
