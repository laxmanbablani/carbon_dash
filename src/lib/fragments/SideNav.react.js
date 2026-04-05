import React from 'react';
import { SideNav as CarbonSideNav } from '@carbon/react';

const SideNav = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSideNav
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSideNav>
    );
};



export default SideNav;
