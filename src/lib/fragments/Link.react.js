import React from 'react';
import { Link as CarbonLink } from '@carbon/react';

const Link = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonLink
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonLink>
    );
};



export default Link;
