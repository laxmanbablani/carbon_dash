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
    TableSelectAll,
    TableSelectRow,
    TableExpandHeader,
    TableExpandRow,
    TableExpandedRow,
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

    const renderTableFixed = (renderProps) => {
        const {
            rows = [],
            headers = [],
            getHeaderProps = () => ({}),
            getRowProps = () => ({}),
            getSelectionProps = () => ({}),
            getExpandProps = () => ({}),
            getTableProps = () => ({}),
            getTableContainerProps = () => ({}),
        } = renderProps;
        console.log('DataTable render prop called', { withExpansion, withSelection });
        
        // Ensure getExpandProps is passed correctly to TableExpandRow
        const rowsToRender = rows.map((row) => {
            const expandProps = withExpansion ? getExpandProps({ row }) : {};
            const rowProps = getRowProps({ row });
            const selectionProps = withSelection ? getSelectionProps({ row }) : {};
            
            console.log('Rendering row', row.id, { isExpanded: row.isExpanded, expandProps });
            
            const rowContent = (
                <>
                    {withSelection && (
                        <TableSelectRow {...selectionProps} />
                    )}
                    {(row.cells || []).map((cell) => (
                        <TableCell key={cell.id}>{cell.value}</TableCell>
                    ))}
                </>
            );

            if (withExpansion) {
                return (
                    <React.Fragment key={row.id}>
                        <TableExpandRow {...expandProps} {...rowProps}>
                            {rowContent}
                        </TableExpandRow>
                        {row.isExpanded && (
                            <TableExpandedRow colSpan={headers.length + (withSelection ? 1 : 0) + 1}>
                                {row.description || (row.cells && row.cells.find(c => c.info && c.info.header === 'description') || "No description provided.")}
                            </TableExpandedRow>
                        )}
                    </React.Fragment>
                );
            }

            return (
                <TableRow key={row.id} {...rowProps}>
                    {rowContent}
                </TableRow>
            );
        });

        return (
        <TableContainer
            title={title}
            description={description}
            {...getTableContainerProps()}
        >
            <Table {...getTableProps()} size={size} useZebraStyles={useZebraStyles}>
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
                    {rowsToRender}
                </TableBody>
            </Table>
        </TableContainer>
        );
    };

    return (
        <CarbonDataTable
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            rows={rows}
            headers={headers}
            isSortable={isSortable}
            {...otherProps}
            render={children || renderTableFixed}
        />
    );
};

export default DataTable;
