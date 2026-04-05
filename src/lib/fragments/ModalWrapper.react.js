import React from 'react';
import { ModalWrapper as CarbonModalWrapper } from '@carbon/react';

const ModalWrapper = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonModalWrapper
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonModalWrapper>
    );
};



export default ModalWrapper;
