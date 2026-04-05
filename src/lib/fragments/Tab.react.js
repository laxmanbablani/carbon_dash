import React from 'react';
import { Tab as CarbonTab } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const Tab = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        label = 'Tab',
        disabled = null,
        ...otherProps
    } = props;
    return (
        <CarbonTab
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            label={label}
            disabled={disabled}
            {...otherProps}
        >
            {children}
        </CarbonTab>
    );
};

export default Tab;
