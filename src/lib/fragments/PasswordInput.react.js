import React from 'react';
import { PasswordInput as CarbonPasswordInput } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const PasswordInput = (props) => {
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
        <CarbonPasswordInput
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            value={value}
            {...otherProps}
        >
            {children}
        </CarbonPasswordInput>
    );
};

export default PasswordInput;
