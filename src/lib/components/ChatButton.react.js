import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * ChatButton is a wrapper for the Carbon ChatButton component.
 */
export default class ChatButton extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['ChatButton'];
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

ChatButton.defaultProps = {
    className: '',
};

ChatButton.propTypes = {
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
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * isQuickAction
     */
    isQuickAction: PropTypes.any,

    /**
     * isSelected
     */
    isSelected: PropTypes.any,

    /**
     * kind
     */
    kind: PropTypes.any,

    /**
     * renderIcon
     */
    renderIcon: PropTypes.node,

    /**
     * size
     */
    size: PropTypes.any,

};
