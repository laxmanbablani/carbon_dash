import React from 'react';
import { PopoverContent as CarbonPopoverContent } from '@carbon/react';

const PopoverContent = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonPopoverContent
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonPopoverContent>
    );
};



export default PopoverContent;
