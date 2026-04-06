import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * TableSelectAll is a wrapper for the Carbon TableSelectAll component.
 */
export default class TableSelectAll extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { checked } = this.props;

        const RealComponent = LazyLoader['TableSelectAll'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    checked={checked}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

TableSelectAll.defaultProps = {
    className: '',
    checked: false,
};

TableSelectAll.propTypes = {
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

    /** n_blur */
    n_blur: PropTypes.number,

    /** n_submit */
    n_submit: PropTypes.number,

    /** debounce */
    debounce: PropTypes.oneOfType([PropTypes.bool, PropTypes.number]),

    /**
     * ariaLabel
     */
    ariaLabel: PropTypes.any,

    /**
     * checked
     */
    checked: PropTypes.bool,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * indeterminate
     */
    indeterminate: PropTypes.any,

    /**
     * name
     */
    name: PropTypes.any,

    /**
     * onSelect
     */
    onSelect: PropTypes.any,

};
