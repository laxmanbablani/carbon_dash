import React from 'react';
import { HeaderMenuItem as CarbonHeaderMenuItem } from '@carbon/react';

const HeaderMenuItem = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonHeaderMenuItem
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonHeaderMenuItem>
    );
};



export default HeaderMenuItem;
