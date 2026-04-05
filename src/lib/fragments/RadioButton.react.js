import React from 'react';
import { RadioButton as CarbonRadioButton } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const RadioButton = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        checked = null,
        label = 'Radio Button',
        value = '',
        ...otherProps
    } = props;
    const onChange = (...args) => {
        if (setProps) {
            setProps({
                checked: args[0].target.checked,
            });
        }
    };

    return (
        <CarbonRadioButton
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            checked={checked}
            labelText={label}
            value={value}
            onChange={onChange}
            {...otherProps}
        >
            {children}
        </CarbonRadioButton>
    );
};

export default RadioButton;
