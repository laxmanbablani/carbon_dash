import React from 'react';
import { MenuItem as CarbonMenuItem } from '@carbon/react';

const MenuItem = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonMenuItem
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonMenuItem>
    );
};



export default MenuItem;
