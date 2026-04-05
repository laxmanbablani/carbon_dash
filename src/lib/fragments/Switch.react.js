import React from 'react';
import { Switch as CarbonSwitch } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const Switch = (props) => {
    const {
        id,
        setProps,
        children,
        className = '',
        loading_state,
        style,
        selected = null,
        ...otherProps
    } = props;
    return (
        <CarbonSwitch
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            selected={selected}
            {...otherProps}
        >
            {children}
        </CarbonSwitch>
    );
};

export default Switch;
