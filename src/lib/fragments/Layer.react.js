import React from 'react';
import { Layer as CarbonLayer } from '@carbon/react';

const Layer = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonLayer
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonLayer>
    );
};



export default Layer;
