import React from 'react';
import { FluidSearch as CarbonFluidSearch } from '@carbon/react';

const FluidSearch = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFluidSearch
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFluidSearch>
    );
};



export default FluidSearch;
