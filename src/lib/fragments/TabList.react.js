import React from 'react';
import { TabList as CarbonTabList } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const TabList = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        contained = null,
        ...otherProps
    } = props;
    return (
        <CarbonTabList
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            contained={contained}
            {...otherProps}
        >
            {children}
        </CarbonTabList>
    );
};

export default TabList;
