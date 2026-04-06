import React from 'react';
import { TableSelectAll as CarbonTableSelectAll } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const TableSelectAll = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        checked = null,
        ...otherProps
    } = props;
    const onSelect = (...args) => {
        if (setProps) {
            setProps({
                checked: !checked,
            });
        }
    };

    return (
        <CarbonTableSelectAll
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            checked={checked}
            onSelect={onSelect}
            {...otherProps}
        >
            {children}
        </CarbonTableSelectAll>
    );
};

export default TableSelectAll;
