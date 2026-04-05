import React from 'react';
import { Checkbox as CarbonCheckbox } from '@carbon/react';

const Checkbox = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        checked,
        label,
        ...otherProps
    } = props;
    const onChange = (...args) => {
        if (setProps) {
            setProps({
                checked: args[1].checked,
            });
        }
    };

    return (
        <CarbonCheckbox
            id={id}
            className={className}
            style={style}
            checked={checked}
            labelText={label}
            onChange={onChange}
            {...otherProps}
        >
            {children}
        </CarbonCheckbox>
    );
};



export default Checkbox;
