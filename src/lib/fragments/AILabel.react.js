import React from 'react';
import { AILabel as CarbonAILabel } from '@carbon/react';

const AILabel = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonAILabel
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonAILabel>
    );
};



export default AILabel;
