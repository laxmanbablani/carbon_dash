import React from 'react';
import { ChatButtonSkeleton as CarbonChatButtonSkeleton } from '@carbon/react';

const ChatButtonSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonChatButtonSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonChatButtonSkeleton>
    );
};



export default ChatButtonSkeleton;
