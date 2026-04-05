import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * TreeNode is a wrapper for the Carbon TreeNode component.
 */
export default class TreeNode extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['TreeNode'];
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

TreeNode.defaultProps = {
    className: '',
};

TreeNode.propTypes = {
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
     * active
     */
    active: PropTypes.any,

    /**
     * defaultIsExpanded
     */
    defaultIsExpanded: PropTypes.any,

    /**
     * depth
     */
    depth: PropTypes.any,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * isExpanded
     */
    isExpanded: PropTypes.any,

    /**
     * label
     */
    label: PropTypes.any,

    /**
     * onNodeFocusEvent
     */
    onNodeFocusEvent: PropTypes.any,

    /**
     * onSelect
     */
    onSelect: PropTypes.any,

    /**
     * onToggle
     */
    onToggle: PropTypes.any,

    /**
     * onTreeSelect
     */
    onTreeSelect: PropTypes.any,

    /**
     * renderIcon
     */
    renderIcon: PropTypes.any,

    /**
     * selected
     */
    selected: PropTypes.any,

    /**
     * value
     */
    value: PropTypes.any,

    /**
     * href
     */
    href: PropTypes.any,

    /**
     * align
     */
    align: PropTypes.any,

    /**
     * autoAlign
     */
    autoAlign: PropTypes.any,

};
