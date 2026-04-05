import React from 'react';
import { ExpandableTile as CarbonExpandableTile } from '@carbon/react';

const ExpandableTile = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonExpandableTile
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonExpandableTile>
    );
};



export default ExpandableTile;
