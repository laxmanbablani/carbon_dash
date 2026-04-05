import React from 'react';
import { ToastNotification as CarbonToastNotification } from '@carbon/react';

const ToastNotification = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonToastNotification
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonToastNotification>
    );
};



export default ToastNotification;
