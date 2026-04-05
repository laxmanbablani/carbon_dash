import React from 'react';
import { FeatureFlags as CarbonFeatureFlags } from '@carbon/react';

const FeatureFlags = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFeatureFlags
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFeatureFlags>
    );
};



export default FeatureFlags;
