import React from 'react';
import { SwitcherDivider as CarbonSwitcherDivider } from '@carbon/react';

const SwitcherDivider = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSwitcherDivider
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSwitcherDivider>
    );
};



export default SwitcherDivider;
