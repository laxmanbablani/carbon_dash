import React from 'react';
import { AILabelActions as CarbonAILabelActions } from '@carbon/react';

const AILabelActions = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonAILabelActions
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonAILabelActions>
    );
};



export default AILabelActions;
