import React from 'react';
import { TextArea as CarbonTextArea } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const TextArea = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        value = '',
        label = 'Text Area',
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
        <CarbonTextArea
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
        </CarbonTextArea>
    );
};

export default TextArea;
