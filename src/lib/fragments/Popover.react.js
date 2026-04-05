import React from 'react';
import { Popover as CarbonPopover } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const Popover = (props) => {
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
        <CarbonPopover
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            open={open}
            {...otherProps}
        >
            {children}
        </CarbonPopover>
    );
};

export default Popover;
