import React from 'react';
import { ComboButton as CarbonComboButton } from '@carbon/react';

const ComboButton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonComboButton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonComboButton>
    );
};



export default ComboButton;
