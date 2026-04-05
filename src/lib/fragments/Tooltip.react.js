import React from 'react';
import { Tooltip as CarbonTooltip } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const Tooltip = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        align = 'top',
        defaultOpen = null,
        description = 'Tooltip Content',
        ...otherProps
    } = props;
    return (
        <CarbonTooltip
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            align={align}
            defaultOpen={defaultOpen}
            description={description}
            {...otherProps}
        >
            {children}
        </CarbonTooltip>
    );
};

export default Tooltip;
