import React from 'react';
import { SideNavDivider as CarbonSideNavDivider } from '@carbon/react';

const SideNavDivider = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSideNavDivider
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSideNavDivider>
    );
};



export default SideNavDivider;
