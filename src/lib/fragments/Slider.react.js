import React from 'react';
import { Slider as CarbonSlider } from '@carbon/react';

const Slider = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        value,
        min,
        max,
        label,
        ...otherProps
    } = props;
    const onChange = (...args) => {
        if (setProps) {
            setProps({
                value: args[0].value,
            });
        }
    };

    return (
        <CarbonSlider
            id={id}
            className={className}
            style={style}
            value={value}
            min={min}
            max={max}
            labelText={label}
            onChange={onChange}
            {...otherProps}
        >
            {children}
        </CarbonSlider>
    );
};



export default Slider;
