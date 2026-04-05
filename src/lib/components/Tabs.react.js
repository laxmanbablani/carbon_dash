import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Tabs is a wrapper for the Carbon Tabs component.
 */
export default class Tabs extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { selectedIndex } = this.props;

        const RealComponent = LazyLoader['Tabs'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    selectedIndex={selectedIndex}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

Tabs.defaultProps = {
    className: '',
    selectedIndex: 0,
};

Tabs.propTypes = {
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
     * defaultSelectedIndex
     */
    defaultSelectedIndex: PropTypes.any,

    /**
     * dismissable
     */
    dismissable: PropTypes.any,

    /**
     * onChange
     */
    onChange: PropTypes.any,

    /**
     * onTabCloseRequest
     */
    onTabCloseRequest: PropTypes.any,

    /**
     * selectedIndex
     */
    selectedIndex: PropTypes.number,

};
