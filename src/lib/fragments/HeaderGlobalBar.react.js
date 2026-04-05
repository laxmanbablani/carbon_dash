import React from 'react';
import { HeaderGlobalBar as CarbonHeaderGlobalBar } from '@carbon/react';

const HeaderGlobalBar = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonHeaderGlobalBar
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonHeaderGlobalBar>
    );
};



export default HeaderGlobalBar;
