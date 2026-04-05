import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * ActionableNotification is a wrapper for the Carbon ActionableNotification component.
 */
export default class ActionableNotification extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['ActionableNotification'];
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

ActionableNotification.defaultProps = {
    className: '',
};

ActionableNotification.propTypes = {
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
     * actionButtonLabel
     */
    actionButtonLabel: PropTypes.any,

    /**
     * ariaLabel
     */
    ariaLabel: PropTypes.any,

    /**
     * caption
     */
    caption: PropTypes.any,

    /**
     * closeOnEscape
     */
    closeOnEscape: PropTypes.any,

    /**
     * hasFocus
     */
    hasFocus: PropTypes.any,

    /**
     * hideCloseButton
     */
    hideCloseButton: PropTypes.any,

    /**
     * inline
     */
    inline: PropTypes.any,

    /**
     * kind
     */
    kind: PropTypes.any,

    /**
     * lowContrast
     */
    lowContrast: PropTypes.any,

    /**
     * onActionButtonClick
     */
    onActionButtonClick: PropTypes.any,

    /**
     * onClose
     */
    onClose: PropTypes.any,

    /**
     * onCloseButtonClick
     */
    onCloseButtonClick: PropTypes.any,

    /**
     * role
     */
    role: PropTypes.any,

    /**
     * statusIconDescription
     */
    statusIconDescription: PropTypes.any,

    /**
     * subtitle
     */
    subtitle: PropTypes.any,

    /**
     * title
     */
    title: PropTypes.any,

};
