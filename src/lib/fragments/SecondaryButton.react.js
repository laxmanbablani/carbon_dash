import React from 'react';
import { SecondaryButton as CarbonSecondaryButton } from '@carbon/react';

const SecondaryButton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSecondaryButton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSecondaryButton>
    );
};



export default SecondaryButton;
