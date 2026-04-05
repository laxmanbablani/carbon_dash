import React from 'react';
import { Checkbox as CarbonCheckbox } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const Checkbox = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        checked = null,
        label = 'Checkbox',
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
            data-dash-is-loading={getLoadingState(loading_state)}
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
