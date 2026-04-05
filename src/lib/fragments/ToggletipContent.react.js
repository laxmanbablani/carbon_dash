import React from 'react';
import { ToggletipContent as CarbonToggletipContent } from '@carbon/react';

const ToggletipContent = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonToggletipContent
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonToggletipContent>
    );
};



export default ToggletipContent;
