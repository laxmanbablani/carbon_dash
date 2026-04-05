import React from 'react';
import { HeaderMenu as CarbonHeaderMenu } from '@carbon/react';

const HeaderMenu = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonHeaderMenu
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonHeaderMenu>
    );
};



export default HeaderMenu;
