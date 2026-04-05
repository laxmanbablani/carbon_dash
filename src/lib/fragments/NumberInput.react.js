import React from 'react';
import { NumberInput as CarbonNumberInput } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const NumberInput = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        value = null,
        label = 'Number Input',
        ...otherProps
    } = props;
    const onChange = (...args) => {
        if (setProps) {
            setProps({
                value: args[1].value,
            });
        }
    };

    return (
        <CarbonNumberInput
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            value={value}
            label={label}
            onChange={onChange}
            {...otherProps}
        >
            {children}
        </CarbonNumberInput>
    );
};

export default NumberInput;
