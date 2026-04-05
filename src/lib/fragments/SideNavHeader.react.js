import React from 'react';
import { SideNavHeader as CarbonSideNavHeader } from '@carbon/react';

const SideNavHeader = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSideNavHeader
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSideNavHeader>
    );
};



export default SideNavHeader;
