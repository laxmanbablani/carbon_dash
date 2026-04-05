import React from 'react';
import { Menu as CarbonMenu } from '@carbon/react';

const Menu = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonMenu
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonMenu>
    );
};



export default Menu;
