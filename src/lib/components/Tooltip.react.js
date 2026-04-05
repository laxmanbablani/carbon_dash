import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Tooltip is a wrapper for the Carbon Tooltip component.
 */
export default class Tooltip extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { align } = this.props;
        const { defaultOpen } = this.props;
        const { description } = this.props;

        const RealComponent = LazyLoader['Tooltip'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    align={align}
                    defaultOpen={defaultOpen}
                    description={description}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

Tooltip.defaultProps = {
    className: '',
    align: 'top',
    defaultOpen: false,
    description: 'Tooltip Content',
};

Tooltip.propTypes = {
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
    align: PropTypes.string,

    /**
     * closeOnActivation
     */
    closeOnActivation: PropTypes.any,

    /**
     * defaultOpen
     */
    defaultOpen: PropTypes.bool,

    /**
     * description
     */
    description: PropTypes.string,

    /**
     * dropShadow
     */
    dropShadow: PropTypes.any,

    /**
     * enterDelayMs
     */
    enterDelayMs: PropTypes.any,

    /**
     * highContrast
     */
    highContrast: PropTypes.any,

    /**
     * label
     */
    label: PropTypes.any,

    /**
     * leaveDelayMs
     */
    leaveDelayMs: PropTypes.any,

};
