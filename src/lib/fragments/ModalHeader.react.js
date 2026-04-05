import React from 'react';
import { ModalHeader as CarbonModalHeader } from '@carbon/react';

const ModalHeader = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonModalHeader
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonModalHeader>
    );
};



export default ModalHeader;
