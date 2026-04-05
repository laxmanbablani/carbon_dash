import React from 'react';
import { HeaderNavigation as CarbonHeaderNavigation } from '@carbon/react';

const HeaderNavigation = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonHeaderNavigation
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonHeaderNavigation>
    );
};



export default HeaderNavigation;
