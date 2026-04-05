import React from 'react';
import { MultiSelect as CarbonMultiSelect } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const MultiSelect = (props) => {
    const {
        id,
        setProps,
        children,
        className = '',
        loading_state,
        style,
        open = null,
        ...otherProps
    } = props;
    return (
        <CarbonMultiSelect
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            open={open}
            {...otherProps}
        >
            {children}
        </CarbonMultiSelect>
    );
};

export default MultiSelect;
