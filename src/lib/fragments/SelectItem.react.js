import React from 'react';
import { SelectItem as CarbonSelectItem } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const SelectItem = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        value = '',
        text = '',
        ...otherProps
    } = props;
    return (
        <CarbonSelectItem
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            value={value}
            text={text}
            {...otherProps}
        >
            {children}
        </CarbonSelectItem>
    );
};

export default SelectItem;
