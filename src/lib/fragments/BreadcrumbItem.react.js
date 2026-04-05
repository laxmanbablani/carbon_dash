import React from 'react';
import { BreadcrumbItem as CarbonBreadcrumbItem } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const BreadcrumbItem = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        href = '#',
        isCurrentPage = null,
        ...otherProps
    } = props;
    return (
        <CarbonBreadcrumbItem
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            href={href}
            isCurrentPage={isCurrentPage}
            {...otherProps}
        >
            {children}
        </CarbonBreadcrumbItem>
    );
};

export default BreadcrumbItem;
