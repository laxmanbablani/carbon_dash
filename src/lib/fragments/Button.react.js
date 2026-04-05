import React from 'react';
import { Button as CarbonButton } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const Button = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        n_clicks = null,
        ...otherProps
    } = props;
    const onClick = (...args) => {
        if (setProps) {
            setProps({
                n_clicks: n_clicks + 1,
            });
        }
    };

    return (
        <CarbonButton
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            n_clicks={n_clicks}
            onClick={onClick}
            {...otherProps}
        >
            {children}
        </CarbonButton>
    );
};

export default Button;
