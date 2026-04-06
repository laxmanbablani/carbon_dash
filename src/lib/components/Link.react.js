import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Link is a wrapper for the Carbon Link component.
 */
export default class Link extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['Link'];
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

Link.defaultProps = {
    className: '',
};

Link.propTypes = {
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
     * as
     */
    as_: PropTypes.any,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * href
     */
    href: PropTypes.any,

    /**
     * inline
     */
    inline: PropTypes.any,

    /**
     * renderIcon
     */
    renderIcon: PropTypes.node,

    /**
     * size
     */
    size: PropTypes.any,

    /**
     * visited
     */
    visited: PropTypes.any,

};
