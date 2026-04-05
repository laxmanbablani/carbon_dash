import React from 'react';
import { NotificationButton as CarbonNotificationButton } from '@carbon/react';

const NotificationButton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonNotificationButton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonNotificationButton>
    );
};



export default NotificationButton;
