import React from 'react';
import { Slug as CarbonSlug } from '@carbon/react';

const Slug = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSlug
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSlug>
    );
};



export default Slug;
