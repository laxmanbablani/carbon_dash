import React from 'react';
import { SideNavLinkText as CarbonSideNavLinkText } from '@carbon/react';

const SideNavLinkText = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSideNavLinkText
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSideNavLinkText>
    );
};



export default SideNavLinkText;
