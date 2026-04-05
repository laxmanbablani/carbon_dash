import React from 'react';
import { GridSettings as CarbonGridSettings } from '@carbon/react';

const GridSettings = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonGridSettings
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonGridSettings>
    );
};



export default GridSettings;
