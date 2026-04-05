import React from 'react';
import { Content as CarbonContent } from '@carbon/react';

const Content = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonContent
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonContent>
    );
};



export default Content;
