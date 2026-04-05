import React from 'react';
import { FluidDropdown as CarbonFluidDropdown } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const FluidDropdown = (props) => {
    const {
        id,
        setProps,
        children,
        className = '',
        loading_state,
        style,
        selectedItem = null,
        ...otherProps
    } = props;
    return (
        <CarbonFluidDropdown
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            selectedItem={selectedItem}
            {...otherProps}
        >
            {children}
        </CarbonFluidDropdown>
    );
};

export default FluidDropdown;
