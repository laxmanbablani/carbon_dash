import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * MenuButton is a wrapper for the Carbon MenuButton component.
 */
export default class MenuButton extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['MenuButton'];
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

MenuButton.defaultProps = {
    className: '',
};

MenuButton.propTypes = {
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
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * kind
     */
    kind: PropTypes.any,

    /**
     * label
     */
    label: PropTypes.any,

    /**
     * menuAlignment
     */
    menuAlignment: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

    /**
     * tabIndex
     */
    tabIndex: PropTypes.any,

    /**
     * menuBackgroundToken
     */
    menuBackgroundToken: PropTypes.any,

    /**
     * menuBorder
     */
    menuBorder: PropTypes.any,

    /**
     * menuTarget
     */
    menuTarget: PropTypes.any,

};
