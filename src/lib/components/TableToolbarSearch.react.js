import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * TableToolbarSearch is a wrapper for the Carbon TableToolbarSearch component.
 */
export default class TableToolbarSearch extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { expanded } = this.props;

        const RealComponent = LazyLoader['TableToolbarSearch'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    expanded={expanded}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

TableToolbarSearch.defaultProps = {
    className: '',
    expanded: false,
};

TableToolbarSearch.propTypes = {
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
     * defaultExpanded
     */
    defaultExpanded: PropTypes.any,

    /**
     * defaultValue
     */
    defaultValue: PropTypes.any,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * expanded
     */
    expanded: PropTypes.bool,

    /**
     * labelText
     */
    labelText: PropTypes.any,

    /**
     * onBlur
     */
    onBlur: PropTypes.any,

    /**
     * onChange
     */
    onChange: PropTypes.any,

    /**
     * onClear
     */
    onClear: PropTypes.any,

    /**
     * onExpand
     */
    onExpand: PropTypes.any,

    /**
     * onFocus
     */
    onFocus: PropTypes.any,

    /**
     * persistent
     */
    persistent: PropTypes.any,

    /**
     * placeholder
     */
    placeholder: PropTypes.any,

    /**
     * searchContainerClass
     */
    searchContainerClass: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

    /**
     * tabIndex
     */
    tabIndex: PropTypes.any,

    /**
     * translateWithId
     */
    translateWithId: PropTypes.any,

};
