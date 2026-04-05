import React from 'react';
import { SideNavFooter as CarbonSideNavFooter } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const SideNavFooter = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        expanded = null,
        ...otherProps
    } = props;
    return (
        <CarbonSideNavFooter
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            expanded={expanded}
            {...otherProps}
        >
            {children}
        </CarbonSideNavFooter>
    );
};

export default SideNavFooter;
