import React from 'react';
import { ActionableNotification as CarbonActionableNotification } from '@carbon/react';

const ActionableNotification = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonActionableNotification
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonActionableNotification>
    );
};



export default ActionableNotification;
