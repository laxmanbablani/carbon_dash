import React from 'react';
import { ContentSwitcher as CarbonContentSwitcher } from '@carbon/react';

const ContentSwitcher = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonContentSwitcher
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonContentSwitcher>
    );
};



export default ContentSwitcher;
