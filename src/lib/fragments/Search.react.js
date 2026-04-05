import React from 'react';
import { Search as CarbonSearch } from '@carbon/react';

const Search = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSearch
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSearch>
    );
};



export default Search;
