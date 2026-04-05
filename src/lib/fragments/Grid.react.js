import React from 'react';
import { Grid as CarbonGrid } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const Grid = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        condensed = null,
        narrow = null,
        fullWidth = null,
        ...otherProps
    } = props;
    return (
        <CarbonGrid
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            condensed={condensed}
            narrow={narrow}
            fullWidth={fullWidth}
            {...otherProps}
        >
            {children}
        </CarbonGrid>
    );
};

export default Grid;
