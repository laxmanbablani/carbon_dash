import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Grid is a wrapper for the Carbon Grid component.
 */
export default class Grid extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { condensed } = this.props;
        const { narrow } = this.props;
        const { fullWidth } = this.props;

        const RealComponent = LazyLoader['Grid'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    condensed={condensed}
                    narrow={narrow}
                    fullWidth={fullWidth}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

Grid.defaultProps = {
    className: '',
    condensed: false,
    narrow: false,
    fullWidth: false,
};

Grid.propTypes = {
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
     * align
     */
    align: PropTypes.any,

    /**
     * as
     */
    as_: PropTypes.any,

    /**
     * condensed
     */
    condensed: PropTypes.bool,

    /**
     * fullWidth
     */
    fullWidth: PropTypes.bool,

    /**
     * narrow
     */
    narrow: PropTypes.bool,

};
