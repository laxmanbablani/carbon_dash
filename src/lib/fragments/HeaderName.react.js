import React from 'react';
import { HeaderName as CarbonHeaderName } from '@carbon/react';

const HeaderName = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonHeaderName
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonHeaderName>
    );
};



export default HeaderName;
