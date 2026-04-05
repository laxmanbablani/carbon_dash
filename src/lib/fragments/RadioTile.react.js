import React from 'react';
import { RadioTile as CarbonRadioTile } from '@carbon/react';

const RadioTile = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonRadioTile
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonRadioTile>
    );
};



export default RadioTile;
