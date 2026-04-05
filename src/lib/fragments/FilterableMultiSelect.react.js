import React from 'react';
import { FilterableMultiSelect as CarbonFilterableMultiSelect } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const FilterableMultiSelect = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        open = null,
        ...otherProps
    } = props;
    return (
        <CarbonFilterableMultiSelect
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            open={open}
            {...otherProps}
        >
            {children}
        </CarbonFilterableMultiSelect>
    );
};

export default FilterableMultiSelect;
