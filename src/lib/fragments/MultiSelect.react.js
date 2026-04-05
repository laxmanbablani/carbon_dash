import React from 'react';
import { MultiSelect as CarbonMultiSelect } from '@carbon/react';

const MultiSelect = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonMultiSelect
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonMultiSelect>
    );
};



export default MultiSelect;
