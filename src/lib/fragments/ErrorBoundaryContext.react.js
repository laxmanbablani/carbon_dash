import React from 'react';
import { ErrorBoundaryContext as CarbonErrorBoundaryContext } from '@carbon/react';

const ErrorBoundaryContext = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonErrorBoundaryContext
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonErrorBoundaryContext>
    );
};



export default ErrorBoundaryContext;
