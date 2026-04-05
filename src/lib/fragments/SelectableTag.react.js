import React from 'react';
import { SelectableTag as CarbonSelectableTag } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const SelectableTag = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        selected = null,
        ...otherProps
    } = props;
    return (
        <CarbonSelectableTag
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            selected={selected}
            {...otherProps}
        >
            {children}
        </CarbonSelectableTag>
    );
};

export default SelectableTag;
