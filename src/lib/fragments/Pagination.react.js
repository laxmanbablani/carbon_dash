import React from 'react';
import { Pagination as CarbonPagination } from '@carbon/react';

const Pagination = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonPagination
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonPagination>
    );
};



export default Pagination;
