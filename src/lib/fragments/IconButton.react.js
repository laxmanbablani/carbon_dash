import React from 'react';
import { IconButton as CarbonIconButton } from '@carbon/react';

const IconButton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonIconButton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonIconButton>
    );
};



export default IconButton;
