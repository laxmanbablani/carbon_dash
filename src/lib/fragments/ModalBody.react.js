import React from 'react';
import { ModalBody as CarbonModalBody } from '@carbon/react';

const ModalBody = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonModalBody
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonModalBody>
    );
};



export default ModalBody;
