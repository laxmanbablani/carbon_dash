import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * IconIndicator is a wrapper for the Carbon IconIndicator component.
 */
export default class IconIndicator extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['IconIndicator'];
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

IconIndicator.defaultProps = {
    className: '',
};

IconIndicator.propTypes = {
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
     * kind
     */
    kind: PropTypes.any,

    /**
     * label
     */
    label: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

};
