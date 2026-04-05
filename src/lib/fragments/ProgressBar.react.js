import React from 'react';
import { ProgressBar as CarbonProgressBar } from '@carbon/react';

const ProgressBar = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonProgressBar
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonProgressBar>
    );
};



export default ProgressBar;
