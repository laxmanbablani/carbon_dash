import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * IconTab is a wrapper for the Carbon IconTab component.
 */
export default class IconTab extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['IconTab'];
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

IconTab.defaultProps = {
    className: '',
};

IconTab.propTypes = {
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
     * badgeIndicator
     */
    badgeIndicator: PropTypes.any,

    /**
     * defaultOpen
     */
    defaultOpen: PropTypes.any,

    /**
     * enterDelayMs
     */
    enterDelayMs: PropTypes.any,

    /**
     * label
     */
    label: PropTypes.any,

    /**
     * leaveDelayMs
     */
    leaveDelayMs: PropTypes.any,

};
