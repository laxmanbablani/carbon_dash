import React from 'react';
import { Search as CarbonSearch } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const Search = (props) => {
    const {
        id,
        setProps,
        children,
        className = '',
        loading_state,
        style,
        value = '',
        ...otherProps
    } = props;
    return (
        <CarbonSearch
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            value={value}
            {...otherProps}
        >
            {children}
        </CarbonSearch>
    );
};

export default Search;
