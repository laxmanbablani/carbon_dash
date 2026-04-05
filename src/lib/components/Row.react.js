import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Row is a wrapper for the Carbon Row component.
 */
export default class Row extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { condensed } = this.props;
        const { narrow } = this.props;

        const RealComponent = LazyLoader['Row'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    condensed={condensed}
                    narrow={narrow}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

Row.defaultProps = {
    className: '',
    condensed: false,
    narrow: false,
};

Row.propTypes = {
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
     * condensed
     */
    condensed: PropTypes.bool,

    /**
     * narrow
     */
    narrow: PropTypes.bool,

};
