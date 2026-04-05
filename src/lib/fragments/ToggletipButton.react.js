import React from 'react';
import { ToggletipButton as CarbonToggletipButton } from '@carbon/react';

const ToggletipButton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonToggletipButton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonToggletipButton>
    );
};



export default ToggletipButton;
