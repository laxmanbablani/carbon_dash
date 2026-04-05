import React from 'react';
import { CodeSnippet as CarbonCodeSnippet } from '@carbon/react';

const CodeSnippet = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonCodeSnippet
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonCodeSnippet>
    );
};



export default CodeSnippet;
