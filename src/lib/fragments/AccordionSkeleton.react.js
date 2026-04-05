import React from 'react';
import { AccordionSkeleton as CarbonAccordionSkeleton } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const AccordionSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        open = null,
        ...otherProps
    } = props;
    return (
        <CarbonAccordionSkeleton
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            open={open}
            {...otherProps}
        >
            {children}
        </CarbonAccordionSkeleton>
    );
};

export default AccordionSkeleton;
