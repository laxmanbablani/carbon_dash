import React from 'react';
import { Toggle as CarbonToggle } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const Toggle = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        toggled = null,
        label = 'Toggle',
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
            data-dash-is-loading={getLoadingState(loading_state)}
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
