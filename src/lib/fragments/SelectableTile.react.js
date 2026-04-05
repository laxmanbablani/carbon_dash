import React from 'react';
import { SelectableTile as CarbonSelectableTile } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const SelectableTile = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        value = '',
        selected = null,
        ...otherProps
    } = props;
    return (
        <CarbonSelectableTile
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            value={value}
            selected={selected}
            {...otherProps}
        >
            {children}
        </CarbonSelectableTile>
    );
};

export default SelectableTile;
