import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Filename is a wrapper for the Carbon Filename component.
 */
export default class Filename extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['Filename'];
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

Filename.defaultProps = {
    className: '',
};

Filename.propTypes = {
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
     * invalid
     */
    invalid: PropTypes.any,

    /**
     * name
     */
    name: PropTypes.any,

    /**
     * status
     */
    status: PropTypes.any,

    /**
     * tabIndex
     */
    tabIndex: PropTypes.any,

};
