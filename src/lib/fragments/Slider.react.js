import React from 'react';
import { Slider as CarbonSlider } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const Slider = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        value = null,
        min = null,
        max = 100,
        label = 'Slider',
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
            data-dash-is-loading={getLoadingState(loading_state)}
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
