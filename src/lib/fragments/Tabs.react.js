import React from 'react';
import { Tabs as CarbonTabs } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const Tabs = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        selectedIndex = null,
        ...otherProps
    } = props;
    const onChange = (...args) => {
        if (setProps) {
            setProps({
                selectedIndex: args[0].selectedIndex,
            });
        }
    };

    return (
        <CarbonTabs
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            selectedIndex={selectedIndex}
            onChange={onChange}
            {...otherProps}
        >
            {children}
        </CarbonTabs>
    );
};

export default Tabs;
