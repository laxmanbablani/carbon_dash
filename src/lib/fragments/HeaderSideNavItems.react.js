import React from 'react';
import { HeaderSideNavItems as CarbonHeaderSideNavItems } from '@carbon/react';

const HeaderSideNavItems = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonHeaderSideNavItems
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonHeaderSideNavItems>
    );
};



export default HeaderSideNavItems;
