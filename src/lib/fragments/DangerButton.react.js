import React from 'react';
import { DangerButton as CarbonDangerButton } from '@carbon/react';

const DangerButton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonDangerButton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonDangerButton>
    );
};



export default DangerButton;
