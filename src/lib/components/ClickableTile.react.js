import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * ClickableTile is a wrapper for the Carbon ClickableTile component.
 */
export default class ClickableTile extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['ClickableTile'];
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

ClickableTile.defaultProps = {
    className: '',
};

ClickableTile.propTypes = {
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
     * clicked
     */
    clicked: PropTypes.any,

    /**
     * decorator
     */
    decorator: PropTypes.any,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * hasRoundedCorners
     */
    hasRoundedCorners: PropTypes.any,

    /**
     * href
     */
    href: PropTypes.any,

    /**
     * light
     */
    light: PropTypes.any,

    /**
     * onClick
     */
    onClick: PropTypes.any,

    /**
     * onKeyDown
     */
    onKeyDown: PropTypes.any,

    /**
     * rel
     */
    rel: PropTypes.any,

    /**
     * renderIcon
     */
    renderIcon: PropTypes.any,

};
