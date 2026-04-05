import React from 'react';
import { TabsVertical as CarbonTabsVertical } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const TabsVertical = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        selectedIndex = -1,
        ...otherProps
    } = props;
    return (
        <CarbonTabsVertical
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            selectedIndex={selectedIndex}
            {...otherProps}
        >
            {children}
        </CarbonTabsVertical>
    );
};

export default TabsVertical;
