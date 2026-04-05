import React from 'react';
import { NumberInput as CarbonNumberInput } from '@carbon/react';

const NumberInput = (props) => {
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
                value: args[1].value,
            });
        }
    };

    return (
        <CarbonNumberInput
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
