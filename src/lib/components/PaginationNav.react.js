import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * PaginationNav is a wrapper for the Carbon PaginationNav component.
 */
export default class PaginationNav extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['PaginationNav'];
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

PaginationNav.defaultProps = {
    className: '',
};

PaginationNav.propTypes = {
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
     * disableOverflow
     */
    disableOverflow: PropTypes.any,

    /**
     * itemsShown
     */
    itemsShown: PropTypes.any,

    /**
     * loop
     */
    loop: PropTypes.any,

    /**
     * onChange
     */
    onChange: PropTypes.any,

    /**
     * page
     */
    page: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

    /**
     * tooltipAlignment
     */
    tooltipAlignment: PropTypes.any,

    /**
     * tooltipPosition
     */
    tooltipPosition: PropTypes.any,

    /**
     * totalItems
     */
    totalItems: PropTypes.any,

    /**
     * translateWithId
     */
    translateWithId: PropTypes.any,

};
