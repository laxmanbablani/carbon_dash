import React from 'react';
import { SideNavItems as CarbonSideNavItems } from '@carbon/react';

const SideNavItems = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSideNavItems
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSideNavItems>
    );
};



export default SideNavItems;
