import React from 'react';
import { SideNavFooter as CarbonSideNavFooter } from '@carbon/react';

const SideNavFooter = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSideNavFooter
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSideNavFooter>
    );
};



export default SideNavFooter;
