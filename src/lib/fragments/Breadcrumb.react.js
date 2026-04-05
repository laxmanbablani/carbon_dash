import React from 'react';
import { Breadcrumb as CarbonBreadcrumb } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const Breadcrumb = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        noTrailingSlash = null,
        ...otherProps
    } = props;
    return (
        <CarbonBreadcrumb
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            noTrailingSlash={noTrailingSlash}
            {...otherProps}
        >
            {children}
        </CarbonBreadcrumb>
    );
};

export default Breadcrumb;
