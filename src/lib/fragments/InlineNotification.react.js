import React from 'react';
import { InlineNotification as CarbonInlineNotification } from '@carbon/react';

const InlineNotification = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonInlineNotification
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonInlineNotification>
    );
};



export default InlineNotification;
