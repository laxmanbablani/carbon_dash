import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * NotificationButton is a wrapper for the Carbon NotificationButton component.
 */
export default class NotificationButton extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['NotificationButton'];
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

NotificationButton.defaultProps = {
    className: '',
};

NotificationButton.propTypes = {
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
     * ariaLabel
     */
    ariaLabel: PropTypes.any,

    /**
     * name
     */
    name: PropTypes.any,

    /**
     * notificationType
     */
    notificationType: PropTypes.any,

    /**
     * renderIcon
     */
    renderIcon: PropTypes.any,

    /**
     * type
     */
    type: PropTypes.any,

};
