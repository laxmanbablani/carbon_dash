import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * TableExpandRow is a wrapper for the Carbon TableExpandRow component.
 */
export default class TableExpandRow extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { isExpanded } = this.props;

        const RealComponent = LazyLoader['TableExpandRow'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    isExpanded={isExpanded}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

TableExpandRow.defaultProps = {
    className: '',
    isExpanded: false,
};

TableExpandRow.propTypes = {
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

    /** persistence */
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),

    /** persisted_props */
    persisted_props: PropTypes.arrayOf(PropTypes.string),

    /** persistence_type */
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),

    /**
     * ariaLabel
     */
    ariaLabel: PropTypes.any,

    /**
     * expandHeader
     */
    expandHeader: PropTypes.any,

    /**
     * expandIconDescription
     */
    expandIconDescription: PropTypes.any,

    /**
     * isExpanded
     */
    isExpanded: PropTypes.bool,

    /**
     * isSelected
     */
    isSelected: PropTypes.any,

    /**
     * onExpand
     */
    onExpand: PropTypes.any,

};
