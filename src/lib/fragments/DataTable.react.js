import React from 'react';
import {
    DataTable as CarbonDataTable,
    Table,
    TableHead,
    TableRow,
    TableHeader,
    TableBody,
    TableCell,
    TableContainer,
} from '@carbon/react';
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

    if (rows.length > 0 && headers.length > 0) {
        return (
            <CarbonDataTable
                rows={rows}
                headers={headers}
                isSortable={isSortable}
                useZebraStyles={useZebraStyles}
                size={size}
                render={({
                    rows,
                    headers,
                    getHeaderProps,
                    getRowProps,
                    getTableProps,
                    getTableContainerProps,
                }) => (
                    <TableContainer
                        title={title}
                        description={description}
                        {...getTableContainerProps()}
                        id={id}
                        className={className}
                        style={style}
                        data-dash-is-loading={getLoadingState(loading_state)}
                    >
                        <Table {...getTableProps()} {...otherProps}>
                            <TableHead>
                                <TableRow>
                                    {headers.map((header) => (
                                        <TableHeader {...getHeaderProps({ header })}>
                                            {header.header}
                                        </TableHeader>
                                    ))}
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {rows.map((row) => (
                                    <TableRow {...getRowProps({ row })}>
                                        {row.cells.map((cell) => (
                                            <TableCell key={cell.id}>{cell.value}</TableCell>
                                        ))}
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                    </TableContainer>
                )}
            />
        );
    }

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
