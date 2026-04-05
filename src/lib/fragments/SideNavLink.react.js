import React from 'react';
import { SideNavLink as CarbonSideNavLink } from '@carbon/react';

const SideNavLink = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSideNavLink
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSideNavLink>
    );
};



export default SideNavLink;
