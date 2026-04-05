import React from 'react';
import { HeaderContainer as CarbonHeaderContainer } from '@carbon/react';

const HeaderContainer = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonHeaderContainer
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonHeaderContainer>
    );
};



export default HeaderContainer;
