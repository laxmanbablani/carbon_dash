import React from 'react';
import { TextInput as CarbonTextInput, AILabel } from '@carbon/react';

const TextInput = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        value,
        ai_label,
        label,
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
