import React from 'react';
import { DataTable as CarbonDataTable } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const DataTable = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        rows = [],
        headers = [],
        useZebraStyles = null,
        size = 'lg',
        title = '',
        description = '',
        isSortable = null,
        withSelection = null,
        withExpansion = null,
        ...otherProps
    } = props;
    return (
        <CarbonDataTable
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            rows={rows}
            headers={headers}
            useZebraStyles={useZebraStyles}
            size={size}
            title={title}
            description={description}
            isSortable={isSortable}
            withSelection={withSelection}
            withExpansion={withExpansion}
            {...otherProps}
        >
            {children}
        </CarbonDataTable>
    );
};

export default DataTable;
