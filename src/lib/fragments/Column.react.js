import React from 'react';
import { Column as CarbonColumn } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const Column = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        sm = null,
        md = null,
        lg = null,
        xlg = null,
        max = null,
        ...otherProps
    } = props;
    return (
        <CarbonColumn
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            sm={sm}
            md={md}
            lg={lg}
            xlg={xlg}
            max={max}
            {...otherProps}
        >
            {children}
        </CarbonColumn>
    );
};

export default Column;
