import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Table is a wrapper for the Carbon Table component.
 */
export default class Table extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['Table'];
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

Table.defaultProps = {
    className: '',
};

Table.propTypes = {
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
     * isSortable
     */
    isSortable: PropTypes.any,

    /**
     * overflowMenuOnHover
     */
    overflowMenuOnHover: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

    /**
     * stickyHeader
     */
    stickyHeader: PropTypes.any,

    /**
     * useStaticWidth
     */
    useStaticWidth: PropTypes.any,

    /**
     * useZebraStyles
     */
    useZebraStyles: PropTypes.any,

    /**
     * tabIndex
     */
    tabIndex: PropTypes.any,

};
