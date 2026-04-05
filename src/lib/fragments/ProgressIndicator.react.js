import React from 'react';
import { ProgressIndicator as CarbonProgressIndicator } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const ProgressIndicator = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        currentIndex = null,
        vertical = null,
        spaceEqually = null,
        ...otherProps
    } = props;
    return (
        <CarbonProgressIndicator
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            currentIndex={currentIndex}
            vertical={vertical}
            spaceEqually={spaceEqually}
            {...otherProps}
        >
            {children}
        </CarbonProgressIndicator>
    );
};

export default ProgressIndicator;
