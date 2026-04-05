import React from 'react';
import { ModalFooter as CarbonModalFooter } from '@carbon/react';

const ModalFooter = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonModalFooter
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonModalFooter>
    );
};



export default ModalFooter;
