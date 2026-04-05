import React from 'react';
import { TableExpandedRow as CarbonTableExpandedRow } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const TableExpandedRow = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTableExpandedRow
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTableExpandedRow>
    );
};

export default TableExpandedRow;
