import React from 'react';
import { SideNavDetails as CarbonSideNavDetails } from '@carbon/react';

const SideNavDetails = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSideNavDetails
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSideNavDetails>
    );
};



export default SideNavDetails;
