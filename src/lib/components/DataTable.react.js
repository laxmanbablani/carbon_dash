import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * DataTable is a wrapper for the Carbon DataTable component.
 */
export default class DataTable extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { rows } = this.props;
        const { headers } = this.props;
        const { useZebraStyles } = this.props;
        const { size } = this.props;
        const { title } = this.props;
        const { description } = this.props;
        const { isSortable } = this.props;
        const { withSelection } = this.props;
        const { withExpansion } = this.props;

        const RealComponent = LazyLoader['DataTable'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
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
                />
            </React.Suspense>
        );
    }
}

DataTable.defaultProps = {
    className: '',
    rows: [],
    headers: [],
    useZebraStyles: false,
    size: 'lg',
    title: '',
    description: '',
    isSortable: false,
    withSelection: false,
    withExpansion: false,
};

DataTable.propTypes = {
    /** id */
    id: PropTypes.string,

    /** children */
    children: PropTypes.node,

    /** className */
    className: PropTypes.string,

    /** style */
    style: PropTypes.object,

    /** setProps */
    setProps: PropTypes.func,

    /** loading_state */
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),

    /**
     * experimentalAutoAlign
     */
    experimentalAutoAlign: PropTypes.any,

    /**
     * filterRows
     */
    filterRows: PropTypes.any,

    /**
     * headers
     */
    headers: PropTypes.array,

    /**
     * key
     */
    key: PropTypes.any,

    /**
     * header
     */
    header: PropTypes.any,

    /**
     * isSortable
     */
    isSortable: PropTypes.bool,

    /**
     * locale
     */
    locale: PropTypes.any,

    /**
     * overflowMenuOnHover
     */
    overflowMenuOnHover: PropTypes.any,

    /**
     * radio
     */
    radio: PropTypes.any,

    /**
     * render
     */
    render: PropTypes.any,

    /**
     * rows
     */
    rows: PropTypes.array,

    /**
     * size
     */
    size: PropTypes.string,

    /**
     * sortRow
     */
    sortRow: PropTypes.any,

    /**
     * stickyHeader
     */
    stickyHeader: PropTypes.any,

    /**
     * translateWithId
     */
    translateWithId: PropTypes.any,

    /**
     * useStaticWidth
     */
    useStaticWidth: PropTypes.any,

    /**
     * useZebraStyles
     */
    useZebraStyles: PropTypes.bool,

    /**
     * title
     */
    title: PropTypes.string,

    /**
     * description
     */
    description: PropTypes.string,

    /**
     * withSelection
     */
    withSelection: PropTypes.bool,

    /**
     * withExpansion
     */
    withExpansion: PropTypes.bool,

};
