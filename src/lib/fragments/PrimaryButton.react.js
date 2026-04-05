import React from 'react';
import { PrimaryButton as CarbonPrimaryButton } from '@carbon/react';

const PrimaryButton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonPrimaryButton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonPrimaryButton>
    );
};



export default PrimaryButton;
