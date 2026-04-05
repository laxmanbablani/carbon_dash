import React from 'react';
import { ChatButton as CarbonChatButton } from '@carbon/react';

const ChatButton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonChatButton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonChatButton>
    );
};



export default ChatButton;
