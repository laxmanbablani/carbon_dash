import React from 'react';
import { Header as CarbonHeader } from '@carbon/react';

const Header = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonHeader
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonHeader>
    );
};



export default Header;
