import React from 'react';
import { SideNav as CarbonSideNav } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const SideNav = (props) => {
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
        <CarbonSideNav
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            expanded={expanded}
            {...otherProps}
        >
            {children}
        </CarbonSideNav>
    );
};

export default SideNav;
