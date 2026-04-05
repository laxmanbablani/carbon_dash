import React from 'react';
import { RadioButtonGroup as CarbonRadioButtonGroup } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const RadioButtonGroup = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        valueSelected = null,
        label = 'Radio Button Group',
        ...otherProps
    } = props;
    const onChange = (...args) => {
        if (setProps) {
            setProps({
                valueSelected: args[0],
            });
        }
    };

    return (
        <CarbonRadioButtonGroup
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            valueSelected={valueSelected}
            labelText={label}
            onChange={onChange}
            {...otherProps}
        >
            {children}
        </CarbonRadioButtonGroup>
    );
};

export default RadioButtonGroup;
