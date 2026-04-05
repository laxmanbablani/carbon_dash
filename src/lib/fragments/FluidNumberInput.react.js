import React from 'react';
import { FluidNumberInput as CarbonFluidNumberInput } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const FluidNumberInput = (props) => {
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
        <CarbonFluidNumberInput
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            value={value}
            {...otherProps}
        >
            {children}
        </CarbonFluidNumberInput>
    );
};

export default FluidNumberInput;
