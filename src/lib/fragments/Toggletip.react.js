import React from 'react';
import { Toggletip as CarbonToggletip } from '@carbon/react';

const Toggletip = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonToggletip
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonToggletip>
    );
};



export default Toggletip;
