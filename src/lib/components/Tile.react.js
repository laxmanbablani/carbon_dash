import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Tile is a wrapper for the Carbon Tile component.
 */
export default class Tile extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['Tile'];
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

Tile.defaultProps = {
    className: '',
};

Tile.propTypes = {
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
     * decorator
     */
    decorator: PropTypes.any,

    /**
     * hasRoundedCorners
     */
    hasRoundedCorners: PropTypes.any,

    /**
     * light
     */
    light: PropTypes.any,

    /**
     * slug
     */
    slug: PropTypes.any,

};
