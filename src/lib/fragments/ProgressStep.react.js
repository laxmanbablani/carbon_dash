import React from 'react';
import { ProgressStep as CarbonProgressStep } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const ProgressStep = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        label = 'Step',
        description = 'Step description',
        secondaryLabel = '',
        disabled = null,
        ...otherProps
    } = props;
    return (
        <CarbonProgressStep
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            label={label}
            description={description}
            secondaryLabel={secondaryLabel}
            disabled={disabled}
            {...otherProps}
        >
            {children}
        </CarbonProgressStep>
    );
};

export default ProgressStep;
