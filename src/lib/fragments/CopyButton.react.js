import React from 'react';
import { CopyButton as CarbonCopyButton } from '@carbon/react';

const CopyButton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonCopyButton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonCopyButton>
    );
};



export default CopyButton;
