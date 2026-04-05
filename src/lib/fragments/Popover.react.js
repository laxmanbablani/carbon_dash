import React from 'react';
import { Popover as CarbonPopover } from '@carbon/react';

const Popover = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonPopover
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonPopover>
    );
};



export default Popover;
