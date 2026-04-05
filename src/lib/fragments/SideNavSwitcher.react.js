import React from 'react';
import { SideNavSwitcher as CarbonSideNavSwitcher } from '@carbon/react';

const SideNavSwitcher = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSideNavSwitcher
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSideNavSwitcher>
    );
};



export default SideNavSwitcher;
