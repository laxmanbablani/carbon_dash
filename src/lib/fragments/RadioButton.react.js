import React from 'react';
import { RadioButton as CarbonRadioButton } from '@carbon/react';

const RadioButton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        checked,
        label,
        value,
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
