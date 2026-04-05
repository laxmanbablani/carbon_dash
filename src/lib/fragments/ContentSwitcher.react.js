import React from 'react';
import { ContentSwitcher as CarbonContentSwitcher } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const ContentSwitcher = (props) => {
    const {
        id,
        setProps,
        children,
        className = '',
        loading_state,
        style,
        selectedIndex = -1,
        ...otherProps
    } = props;
    return (
        <CarbonContentSwitcher
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            selectedIndex={selectedIndex}
            {...otherProps}
        >
            {children}
        </CarbonContentSwitcher>
    );
};

export default ContentSwitcher;
