import React from 'react';
import { RadioTile as CarbonRadioTile } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const RadioTile = (props) => {
    const {
        id,
        setProps,
        children,
        className = '',
        loading_state,
        style,
        value = '',
        checked = null,
        ...otherProps
    } = props;
    return (
        <CarbonRadioTile
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            value={value}
            checked={checked}
            {...otherProps}
        >
            {children}
        </CarbonRadioTile>
    );
};

export default RadioTile;
