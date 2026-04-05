import React from 'react';
import { Menu as CarbonMenu } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const Menu = (props) => {
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
        <CarbonMenu
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            open={open}
            {...otherProps}
        >
            {children}
        </CarbonMenu>
    );
};

export default Menu;
