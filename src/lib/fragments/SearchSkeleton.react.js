import React from 'react';
import { SearchSkeleton as CarbonSearchSkeleton } from '@carbon/react';

const SearchSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSearchSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSearchSkeleton>
    );
};



export default SearchSkeleton;
