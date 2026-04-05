import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * TableBatchActions is a wrapper for the Carbon TableBatchActions component.
 */
export default class TableBatchActions extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['TableBatchActions'];
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

TableBatchActions.defaultProps = {
    className: '',
};

TableBatchActions.propTypes = {
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
     * onCancel
     */
    onCancel: PropTypes.any,

    /**
     * onSelectAll
     */
    onSelectAll: PropTypes.any,

    /**
     * shouldShowBatchActions
     */
    shouldShowBatchActions: PropTypes.any,

    /**
     * totalCount
     */
    totalCount: PropTypes.any,

    /**
     * totalSelected
     */
    totalSelected: PropTypes.any,

    /**
     * translateWithId
     */
    translateWithId: PropTypes.any,

};
