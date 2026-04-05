import React from 'react';
import { FilterableMultiSelect as CarbonFilterableMultiSelect } from '@carbon/react';

const FilterableMultiSelect = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFilterableMultiSelect
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFilterableMultiSelect>
    );
};



export default FilterableMultiSelect;
