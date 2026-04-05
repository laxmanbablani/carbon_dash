import React from 'react';
import { Theme as CarbonTheme } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const Theme = (props) => {
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
        <CarbonTheme
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTheme>
    );
};

export default Theme;
