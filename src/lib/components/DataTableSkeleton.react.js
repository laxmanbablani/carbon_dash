import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * DataTableSkeleton is a wrapper for the Carbon DataTableSkeleton component.
 */
export default class DataTableSkeleton extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['DataTableSkeleton'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

DataTableSkeleton.defaultProps = {
    className: '',
};

DataTableSkeleton.propTypes = {
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
     * columnCount
     */
    columnCount: PropTypes.any,

    /**
     * headers
     */
    headers: PropTypes.any,

    /**
     * rowCount
     */
    rowCount: PropTypes.any,

    /**
     * showHeader
     */
    showHeader: PropTypes.any,

    /**
     * showToolbar
     */
    showToolbar: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

    /**
     * zebra
     */
    zebra: PropTypes.any,

};
