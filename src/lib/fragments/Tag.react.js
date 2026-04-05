import React from 'react';
import { Tag as CarbonTag } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const Tag = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        type = 'gray',
        size = 'md',
        disabled = null,
        ...otherProps
    } = props;
    return (
        <CarbonTag
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            type={type}
            size={size}
            disabled={disabled}
            {...otherProps}
        >
            {children}
        </CarbonTag>
    );
};

export default Tag;
