import React from 'react';
import { RadioButtonGroup as CarbonRadioButtonGroup } from '@carbon/react';

const RadioButtonGroup = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        valueSelected,
        label,
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
