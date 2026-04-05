import React from 'react';
import { ModalPresence as CarbonModalPresence } from '@carbon/react';

const ModalPresence = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonModalPresence
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonModalPresence>
    );
};



export default ModalPresence;
