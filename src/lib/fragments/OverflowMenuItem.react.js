import React from 'react';
import { OverflowMenuItem as CarbonOverflowMenuItem } from '@carbon/react';

const OverflowMenuItem = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonOverflowMenuItem
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonOverflowMenuItem>
    );
};



export default OverflowMenuItem;
