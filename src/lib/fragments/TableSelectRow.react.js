import React from 'react';
import { TableSelectRow as CarbonTableSelectRow } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const TableSelectRow = (props) => {
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

    const onChange = (...args) => {
        if (setProps) {
            setProps({
                checked: args[0],
            });
        }
    };

    return (
        <CarbonTableSelectRow
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            checked={checked}
            onSelect={onSelect}
            onChange={onChange}
            {...otherProps}
        >
            {children}
        </CarbonTableSelectRow>
    );
};

export default TableSelectRow;
