import React from 'react';
import { TableToolbarSearch as CarbonTableToolbarSearch } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const TableToolbarSearch = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        expanded = null,
        ...otherProps
    } = props;
    return (
        <CarbonTableToolbarSearch
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            expanded={expanded}
            {...otherProps}
        >
            {children}
        </CarbonTableToolbarSearch>
    );
};

export default TableToolbarSearch;
