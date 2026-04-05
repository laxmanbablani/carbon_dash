import React from 'react';
import { SwitcherItem as CarbonSwitcherItem } from '@carbon/react';

const SwitcherItem = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSwitcherItem
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSwitcherItem>
    );
};



export default SwitcherItem;
