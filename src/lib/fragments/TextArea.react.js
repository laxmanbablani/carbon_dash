import React from 'react';
import { TextArea as CarbonTextArea } from '@carbon/react';

const TextArea = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        value,
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
        <CarbonTextArea
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
