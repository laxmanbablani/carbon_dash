import React from 'react';
import { ToggletipLabel as CarbonToggletipLabel } from '@carbon/react';

const ToggletipLabel = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonToggletipLabel
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonToggletipLabel>
    );
};



export default ToggletipLabel;
