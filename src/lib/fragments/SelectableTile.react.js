import React from 'react';
import { SelectableTile as CarbonSelectableTile } from '@carbon/react';

const SelectableTile = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSelectableTile
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSelectableTile>
    );
};



export default SelectableTile;
