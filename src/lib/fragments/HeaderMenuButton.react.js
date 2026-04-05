import React from 'react';
import { HeaderMenuButton as CarbonHeaderMenuButton } from '@carbon/react';

const HeaderMenuButton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonHeaderMenuButton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonHeaderMenuButton>
    );
};



export default HeaderMenuButton;
