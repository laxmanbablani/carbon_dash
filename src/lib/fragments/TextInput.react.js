import React from 'react';
import { TextInput as CarbonTextInput, AILabel } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const TextInput = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        value = '',
        ai_label = null,
        label = 'Text Input',
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
        <CarbonTextInput
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            value={value}
            ai_label={ai_label}
            labelText={label}
            onChange={onChange}
            {...otherProps}
        >
            {children}
        </CarbonTextInput>
    );
};

export default TextInput;
