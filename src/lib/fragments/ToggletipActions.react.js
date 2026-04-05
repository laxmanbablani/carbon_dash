import React from 'react';
import { ToggletipActions as CarbonToggletipActions } from '@carbon/react';

const ToggletipActions = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonToggletipActions
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonToggletipActions>
    );
};



export default ToggletipActions;
