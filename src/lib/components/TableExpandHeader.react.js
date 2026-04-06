import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * TableExpandHeader is a wrapper for the Carbon TableExpandHeader component.
 */
export default class TableExpandHeader extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { isExpanded } = this.props;

        const RealComponent = LazyLoader['TableExpandHeader'];
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

TableExpandHeader.defaultProps = {
    className: '',
    isExpanded: false,
};

TableExpandHeader.propTypes = {
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
     * enableExpando
     */
    enableExpando: PropTypes.any,

    /**
     * enableToggle
     */
    enableToggle: PropTypes.any,

    /**
     * expandIconDescription
     */
    expandIconDescription: PropTypes.any,

    /**
     * isExpanded
     */
    isExpanded: PropTypes.bool,

    /**
     * onExpand
     */
    onExpand: PropTypes.any,

};
