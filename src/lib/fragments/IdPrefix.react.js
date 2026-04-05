import React from 'react';
import { IdPrefix as CarbonIdPrefix } from '@carbon/react';

const IdPrefix = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonIdPrefix
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonIdPrefix>
    );
};



export default IdPrefix;
