import React from 'react';
import { ComposedModalPresence as CarbonComposedModalPresence } from '@carbon/react';

const ComposedModalPresence = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonComposedModalPresence
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonComposedModalPresence>
    );
};



export default ComposedModalPresence;
