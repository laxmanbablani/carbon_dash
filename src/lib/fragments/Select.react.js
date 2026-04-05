import React from 'react';
import { Select as CarbonSelect } from '@carbon/react';

const Select = (props) => {
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
        <CarbonSelect
            id={id}
            className={className}
            style={style}
            value={value}
            labelText={label}
            onChange={onChange}
            {...otherProps}
        >
            {children}
        </CarbonSelect>
    );
};



export default Select;
