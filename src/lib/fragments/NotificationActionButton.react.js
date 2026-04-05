import React from 'react';
import { NotificationActionButton as CarbonNotificationActionButton } from '@carbon/react';

const NotificationActionButton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonNotificationActionButton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonNotificationActionButton>
    );
};



export default NotificationActionButton;
