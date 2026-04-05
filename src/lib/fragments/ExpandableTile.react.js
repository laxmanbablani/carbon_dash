import React from 'react';
import { ExpandableTile as CarbonExpandableTile } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const ExpandableTile = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        expanded = null,
        ...otherProps
    } = props;
    return (
        <CarbonExpandableTile
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            expanded={expanded}
            {...otherProps}
        >
            {children}
        </CarbonExpandableTile>
    );
};

export default ExpandableTile;
