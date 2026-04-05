import React from 'react';
import { ExpandableSearch as CarbonExpandableSearch } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const ExpandableSearch = (props) => {
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
        <CarbonExpandableSearch
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            value={value}
            {...otherProps}
        >
            {children}
        </CarbonExpandableSearch>
    );
};

export default ExpandableSearch;
