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
    TableExpandHeader,
    TableExpandRow,
    TableExpandedRow,
    TableSelectAll,
    TableSelectRow
} from '@carbon/react';

const DataTable = (props) => {
    const {
        id,
        setProps,
        children,
        className = '',
        style,
        rows = [],
        headers = [],
        useZebraStyles = false,
        size = 'lg',
        title = '',
        description = '',
        isSortable = false,
        withSelection = false,
        withExpansion = false,
        ...otherProps
    } = props;

    return (
        <CarbonDataTable
            rows={rows}
            headers={headers}
            isSortable={isSortable}
            render={({
                rows,
                headers,
                getHeaderProps,
                getRowProps,
                getTableProps,
                getSelectionProps,
                getExpandProps
            }) => (
                <TableContainer title={title} description={description} className={className} style={style}>
                    <Table {...getTableProps()} useZebraStyles={useZebraStyles} size={size}>
                        <TableHead>
                            <TableRow>
                                {withExpansion && <TableExpandHeader />}
                                {withSelection && (
                                    <TableSelectAll {...getSelectionProps()} />
                                )}
                                {headers.map((header) => (
                                    <TableHeader {...getHeaderProps({ header })}>
                                        {header.header}
                                    </TableHeader>
                                ))}
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {rows.map((row) => (
                                <React.Fragment key={row.id}>
                                    {withExpansion ? (
                                        <TableExpandRow {...getRowProps({ row })} {...getExpandProps({ row })}>
                                            {withSelection && (
                                                <TableSelectRow {...getSelectionProps({ row })} />
                                            )}
                                            {row.cells.map((cell) => (
                                                <TableCell key={cell.id}>{cell.value}</TableCell>
                                            ))}
                                        </TableExpandRow>
                                    ) : (
                                        <TableRow {...getRowProps({ row })}>
                                            {withSelection && (
                                                <TableSelectRow {...getSelectionProps({ row })} />
                                            )}
                                            {row.cells.map((cell) => (
                                                <TableCell key={cell.id}>{cell.value}</TableCell>
                                            ))}
                                        </TableRow>
                                    )}
                                    {withExpansion && row.isExpanded && (
                                        <TableExpandedRow colSpan={headers.length + (withSelection ? 2 : 1)}>
                                            {row.expansionContent || 'No expansion content provided'}
                                        </TableExpandedRow>
                                    )}
                                </React.Fragment>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            )}
            {...otherProps}
        />
    );
};

export default DataTable;
