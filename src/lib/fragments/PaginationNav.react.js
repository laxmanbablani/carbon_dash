import React from 'react';
import { PaginationNav as CarbonPaginationNav } from '@carbon/react';

const PaginationNav = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonPaginationNav
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonPaginationNav>
    );
};



export default PaginationNav;
