import React from 'react';
import { Row as CarbonRow } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const Row = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        condensed = null,
        narrow = null,
        ...otherProps
    } = props;
    return (
        <CarbonRow
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            condensed={condensed}
            narrow={narrow}
            {...otherProps}
        >
            {children}
        </CarbonRow>
    );
};

export default Row;
