import React from 'react';
import { ClickableTile as CarbonClickableTile } from '@carbon/react';

const ClickableTile = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonClickableTile
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonClickableTile>
    );
};



export default ClickableTile;
