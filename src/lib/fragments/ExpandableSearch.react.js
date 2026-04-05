import React from 'react';
import { ExpandableSearch as CarbonExpandableSearch } from '@carbon/react';

const ExpandableSearch = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonExpandableSearch
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonExpandableSearch>
    );
};



export default ExpandableSearch;
