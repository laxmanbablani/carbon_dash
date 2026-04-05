import React from 'react';
import { Toggle as CarbonToggle } from '@carbon/react';

const Toggle = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        toggled,
        label,
        ...otherProps
    } = props;
    const onToggle = (...args) => {
        if (setProps) {
            setProps({
                toggled: args[0],
            });
        }
    };

    return (
        <CarbonToggle
            id={id}
            className={className}
            style={style}
            toggled={toggled}
            labelText={label}
            onToggle={onToggle}
            {...otherProps}
        >
            {children}
        </CarbonToggle>
    );
};



export default Toggle;
