import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Menu is a wrapper for the Carbon Menu component.
 */
export default class Menu extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['Menu'];
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

Menu.defaultProps = {
    className: '',
};

Menu.propTypes = {
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
     * backgroundToken
     */
    backgroundToken: PropTypes.any,

    /**
     * border
     */
    border: PropTypes.any,

    /**
     * label
     */
    label: PropTypes.any,

    /**
     * menuAlignment
     */
    menuAlignment: PropTypes.any,

    /**
     * mode
     */
    mode: PropTypes.any,

    /**
     * onClose
     */
    onClose: PropTypes.any,

    /**
     * onOpen
     */
    onOpen: PropTypes.any,

    /**
     * open
     */
    open: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

    /**
     * target
     */
    target: PropTypes.any,

    /**
     * x
     */
    x: PropTypes.any,

    /**
     * y
     */
    y: PropTypes.any,

};
