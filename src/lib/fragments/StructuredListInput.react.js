import React from 'react';
import { StructuredListInput as CarbonStructuredListInput } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const StructuredListInput = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        value = '',
        ...otherProps
    } = props;
    return (
        <CarbonStructuredListInput
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            value={value}
            {...otherProps}
        >
            {children}
        </CarbonStructuredListInput>
    );
};

export default StructuredListInput;
