import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * TableToolbarMenu is a wrapper for the Carbon TableToolbarMenu component.
 */
export default class TableToolbarMenu extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['TableToolbarMenu'];
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

TableToolbarMenu.defaultProps = {
    className: '',
};

TableToolbarMenu.propTypes = {
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
     * iconDescription
     */
    iconDescription: PropTypes.any,

    /**
     * menuOptionsClass
     */
    menuOptionsClass: PropTypes.any,

    /**
     * renderIcon
     */
    renderIcon: PropTypes.node,

};
