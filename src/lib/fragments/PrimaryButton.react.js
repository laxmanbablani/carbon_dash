import React from 'react';
import { PrimaryButton as CarbonPrimaryButton } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const PrimaryButton = (props) => {
    const {
        id,
        setProps,
        children,
        className = '',
        loading_state,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonPrimaryButton
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonPrimaryButton>
    );
};

export default PrimaryButton;
