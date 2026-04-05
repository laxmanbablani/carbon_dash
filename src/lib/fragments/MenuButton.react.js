import React from 'react';
import { MenuButton as CarbonMenuButton } from '@carbon/react';

const MenuButton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonMenuButton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonMenuButton>
    );
};



export default MenuButton;
