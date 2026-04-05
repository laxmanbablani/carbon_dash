import React from 'react';
import { StaticNotification as CarbonStaticNotification } from '@carbon/react';

const StaticNotification = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonStaticNotification
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonStaticNotification>
    );
};



export default StaticNotification;
