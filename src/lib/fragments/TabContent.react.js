import React from 'react';
import { TabContent as CarbonTabContent } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const TabContent = (props) => {
    const {
        id,
        setProps,
        children,
        className = '',
        loading_state,
        style,
        selected = null,
        ...otherProps
    } = props;
    return (
        <CarbonTabContent
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            selected={selected}
            {...otherProps}
        >
            {children}
        </CarbonTabContent>
    );
};

export default TabContent;
