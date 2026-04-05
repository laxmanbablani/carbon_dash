import React from 'react';
import { Loading as CarbonLoading } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const Loading = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        active = true,
        withOverlay = true,
        small = null,
        ...otherProps
    } = props;
    return (
        <CarbonLoading
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            active={active}
            withOverlay={withOverlay}
            small={small}
            {...otherProps}
        >
            {children}
        </CarbonLoading>
    );
};

export default Loading;
