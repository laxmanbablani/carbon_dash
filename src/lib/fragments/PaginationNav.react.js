import React from 'react';
import { PaginationNav as CarbonPaginationNav } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const PaginationNav = (props) => {
    const {
        id,
        setProps,
        children,
        className = '',
        loading_state,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonPaginationNav
            data-dash-is-loading={getLoadingState(loading_state)}
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
