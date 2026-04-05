import React from 'react';
import { AILabelContent as CarbonAILabelContent } from '@carbon/react';

const AILabelContent = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonAILabelContent
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonAILabelContent>
    );
};



export default AILabelContent;
