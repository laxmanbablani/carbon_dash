import React from 'react';
import { Accordion as CarbonAccordion } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const Accordion = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        align = 'end',
        isFlush = null,
        size = 'md',
        ...otherProps
    } = props;
    return (
        <CarbonAccordion
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            align={align}
            isFlush={isFlush}
            size={size}
            {...otherProps}
        >
            {children}
        </CarbonAccordion>
    );
};

export default Accordion;
