import React from 'react';
import { CodeSnippetSkeleton as CarbonCodeSnippetSkeleton } from '@carbon/react';

const CodeSnippetSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonCodeSnippetSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonCodeSnippetSkeleton>
    );
};



export default CodeSnippetSkeleton;
