import React from 'react';
import { ComposedModal as CarbonComposedModal } from '@carbon/react';

const ComposedModal = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonComposedModal
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonComposedModal>
    );
};



export default ComposedModal;
