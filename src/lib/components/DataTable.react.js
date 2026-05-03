import React, { useState, useMemo } from 'react';
import PropTypes from 'prop-types';
import {
    DataTableSkeleton as CarbonDataTableSkeleton,
    TableContainer as CarbonTableContainer,
    Table as CarbonTable,
    TableHead as CarbonTableHead,
    TableBody as CarbonTableBody,
    TableRow as CarbonTableRow,
    TableHeader as CarbonTableHeader,
    TableCell as CarbonTableCell,
    TableSelectAll as CarbonTableSelectAll,
    TableSelectRow as CarbonTableSelectRow,
    TableToolbar as CarbonTableToolbar,
    TableToolbarContent as CarbonTableToolbarContent,
    TableToolbarSearch as CarbonTableToolbarSearch,
} from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const DataTable = (props) => {
    const {
        id, children, className = '', style = {}, loading_state,
        rows = [], headers = [],
        isSortable = false, useZebraStyles = false,
        withSelection = false, withToolbar = false,
        selectedRows = [],
        title, description,
        stickyHeader = false, size,
        ...others
    } = props;

    if (loading_state && loading_state.is_loading) {
        return (
            <CarbonDataTableSkeleton
                id={id} className={className}
                headers={headers.map(h => ({ header: h.header }))}
                rowCount={rows.length || 3}
            />
        );
    }

    const [sortKey, setSortKey] = useState(null);
    const [sortDirection, setSortDirection] = useState('NONE');
    const [filterText, setFilterText] = useState('');

    const handleHeaderClick = (key) => {
        if (!isSortable) return;
        let newDir = 'ASC';
        if (sortKey === key) {
            newDir = sortDirection === 'ASC' ? 'DESC' : 'ASC';
        }
        setSortKey(key);
        setSortDirection(newDir);
        if (props.setProps) props.setProps({ selectedRows: selectedRows });
    };

    const handleSelectRow = (rowId) => {
        const has = selectedRows.indexOf(rowId) >= 0;
        const newSelected = has
            ? selectedRows.filter(id => id !== rowId)
            : [...selectedRows, rowId];
        if (props.setProps) props.setProps({ selectedRows: newSelected });
    };

    const handleSelectAll = () => {
        const allSelected = filtered.length > 0 && selectedRows.length === filtered.length;
        const newSelected = allSelected ? [] : filtered.map(r => r.id);
        if (props.setProps) props.setProps({ selectedRows: newSelected });
    };

    // Filter
    const filtered = useMemo(() => {
        if (!filterText.trim()) return rows;
        const term = filterText.toLowerCase();
        return rows.filter(row =>
            headers.some(h => String(row[h.key] || '').toLowerCase().includes(term))
        );
    }, [rows, headers, filterText]);

    // Sort
    const sorted = useMemo(() => {
        if (!sortKey || sortDirection === 'NONE') return filtered;
        return [...filtered].sort((a, b) => {
            const va = a[sortKey] == null ? '' : String(a[sortKey]);
            const vb = b[sortKey] == null ? '' : String(b[sortKey]);
            const cmp = va.localeCompare(vb, undefined, { numeric: true });
            return sortDirection === 'ASC' ? cmp : -cmp;
        });
    }, [filtered, sortKey, sortDirection]);

    const allSelected = sorted.length > 0 && selectedRows.length === sorted.length;

    const toolbar = withToolbar ? (
        <CarbonTableToolbar>
            <CarbonTableToolbarContent>
                <CarbonTableToolbarSearch
                    persistent
                    value={filterText}
                    onChange={(e) => setFilterText(e?.target?.value || '')}
                />
            </CarbonTableToolbarContent>
        </CarbonTableToolbar>
    ) : null;

    return (
        <CarbonTableContainer
            id={id} className={className}
            title={title} description={description}
        >
            {toolbar}
            <CarbonTable
                style={style}
                data-dash-is-loading={getLoadingState(loading_state) || undefined}
                useZebraStyles={useZebraStyles}
                size={size}
                stickyHeader={stickyHeader}
                {...others}
            >
                <CarbonTableHead>
                    <CarbonTableRow>
                        {withSelection && (
                            <CarbonTableSelectAll
                                id={`${id}-select-all`}
                                checked={allSelected}
                                indeterminate={selectedRows.length > 0 && !allSelected}
                                onSelect={handleSelectAll}
                            />
                        )}
                        {headers.map((header, i) => (
                            <CarbonTableHeader
                                key={header.key || i}
                                isSortable={isSortable}
                                isSorted={sortKey === header.key}
                                sortDirection={sortKey === header.key
                                    ? (sortDirection === 'ASC' ? 'ASC' : 'DESC')
                                    : 'NONE'
                                }
                                onClick={() => handleHeaderClick(header.key)}
                            >
                                {header.header}
                            </CarbonTableHeader>
                        ))}
                    </CarbonTableRow>
                </CarbonTableHead>
                <CarbonTableBody>
                    {sorted.map((row) => (
                        <CarbonTableRow key={row.id} isSelected={selectedRows.indexOf(row.id) >= 0}>
                            {withSelection && (
                                <CarbonTableSelectRow
                                    id={`${id}-select-${row.id}`}
                                    checked={selectedRows.indexOf(row.id) >= 0}
                                    onSelect={handleSelectRow.bind(null, row.id)}
                                    ariaLabel={`Select row ${row.id}`}
                                />
                            )}
                            {headers.map((header) => (
                                <CarbonTableCell key={`${row.id}-${header.key}`}>
                                    {row[header.key]}
                                </CarbonTableCell>
                            ))}
                        </CarbonTableRow>
                    ))}
                </CarbonTableBody>
            </CarbonTable>
        </CarbonTableContainer>
    );
};

DataTable.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,
    /** Dash-assigned callback */
    setProps: PropTypes.func,
    /** Alternative content */
    children: PropTypes.node,
    /** Custom CSS class */
    className: PropTypes.string,
    /** Inline styles */
    style: PropTypes.object,
    /** Dash loading state */
    loading_state: PropTypes.shape({
        is_loading: PropTypes.bool,
        prop_name: PropTypes.string,
        component_name: PropTypes.string,
    }),
    /** Array of row objects. Each row MUST have a unique `id` string. */
    rows: PropTypes.arrayOf(PropTypes.object),
    /** Array of header configs: {key: string, header: string} */
    headers: PropTypes.arrayOf(PropTypes.shape({
        key: PropTypes.string.isRequired,
        header: PropTypes.node.isRequired,
        isSortable: PropTypes.bool,
    })),
    /** Allow sorting by clicking column headers */
    isSortable: PropTypes.bool,
    /** Show row selection checkboxes */
    withSelection: PropTypes.bool,
    /** Show toolbar with search/filter */
    withToolbar: PropTypes.bool,
    /** Array of selected row IDs (read via Dash callback) */
    selectedRows: PropTypes.arrayOf(PropTypes.string),
    /** Add zebra striping */
    useZebraStyles: PropTypes.bool,
    /** Table title */
    title: PropTypes.string,
    /** Table description */
    description: PropTypes.string,
    /** Make header sticky */
    stickyHeader: PropTypes.bool,
    /** Table size */
    size: PropTypes.oneOf(['xs', 'sm', 'md', 'lg', 'xl', '2xl']),
};

DataTable.defaultProps = {
    rows: [],
    headers: [],
    isSortable: false,
    withSelection: false,
    withToolbar: false,
    selectedRows: [],
    useZebraStyles: false,
};

export default DataTable;
