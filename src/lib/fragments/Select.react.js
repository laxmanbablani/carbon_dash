import React from 'react';
import { Select as CarbonSelect } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const Select = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        value = '',
        label = 'Select',
        ...otherProps
    } = props;
    const onChange = (...args) => {
        if (setProps) {
            setProps({
                value: args[0].target.value,
            });
        }
    };

    return (
        <CarbonSelect
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            value={value}
            labelText={label}
            onChange={onChange}
            {...otherProps}
        >
            {children}
        </CarbonSelect>
    );
};

export default Select;
