import React from 'react';
import { OverflowMenu as CarbonOverflowMenu } from '@carbon/react';

const OverflowMenu = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonOverflowMenu
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonOverflowMenu>
    );
};



export default OverflowMenu;
