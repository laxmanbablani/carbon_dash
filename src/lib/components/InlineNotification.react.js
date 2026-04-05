import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * InlineNotification is a wrapper for the Carbon InlineNotification component.
 */
export default class InlineNotification extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['InlineNotification'];
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

InlineNotification.defaultProps = {
    className: '',
};

InlineNotification.propTypes = {
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
     * hideCloseButton
     */
    hideCloseButton: PropTypes.any,

    /**
     * kind
     */
    kind: PropTypes.any,

    /**
     * lowContrast
     */
    lowContrast: PropTypes.any,

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
