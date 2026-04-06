import React from 'react';
import { TableExpandRow as CarbonTableExpandRow } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const TableExpandRow = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        isExpanded = null,
        ...otherProps
    } = props;
    const onExpand = (...args) => {
        if (setProps) {
            setProps({
                isExpanded: !isExpanded,
            });
        }
    };

    return (
        <CarbonTableExpandRow
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            isExpanded={isExpanded}
            onExpand={onExpand}
            {...otherProps}
        >
            {children}
        </CarbonTableExpandRow>
    );
};

export default TableExpandRow;
