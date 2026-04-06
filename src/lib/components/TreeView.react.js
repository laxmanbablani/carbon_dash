import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * TreeView is a wrapper for the Carbon TreeView component.
 */
export default class TreeView extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { selected } = this.props;
        const { active } = this.props;

        const RealComponent = LazyLoader['TreeView'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    selected={selected}
                    active={active}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

TreeView.defaultProps = {
    className: '',
    selected: null,
    active: null,
};

TreeView.propTypes = {
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
     * active
     */
    active: PropTypes.any,

    /**
     * hideLabel
     */
    hideLabel: PropTypes.any,

    /**
     * label
     */
    label: PropTypes.any,

    /**
     * multiselect
     */
    multiselect: PropTypes.any,

    /**
     * onActivate
     */
    onActivate: PropTypes.any,

    /**
     * onSelect
     */
    onSelect: PropTypes.any,

    /**
     * selected
     */
    selected: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

};
