import React from 'react';
import { MenuItemRadioGroup as CarbonMenuItemRadioGroup } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const MenuItemRadioGroup = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        selectedItem = null,
        ...otherProps
    } = props;
    return (
        <CarbonMenuItemRadioGroup
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            selectedItem={selectedItem}
            {...otherProps}
        >
            {children}
        </CarbonMenuItemRadioGroup>
    );
};

export default MenuItemRadioGroup;
