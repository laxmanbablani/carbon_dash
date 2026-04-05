import React from 'react';
import { ErrorBoundary as CarbonErrorBoundary } from '@carbon/react';

const ErrorBoundary = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonErrorBoundary
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonErrorBoundary>
    );
};



export default ErrorBoundary;
