import React from 'react';
import { FluidComboBox as CarbonFluidComboBox } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const FluidComboBox = (props) => {
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
        <CarbonFluidComboBox
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            selectedItem={selectedItem}
            {...otherProps}
        >
            {children}
        </CarbonFluidComboBox>
    );
};

export default FluidComboBox;
