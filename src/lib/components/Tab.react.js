import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Tab is a wrapper for the Carbon Tab component.
 */
export default class Tab extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { label } = this.props;
        const { disabled } = this.props;

        const RealComponent = LazyLoader['Tab'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    label={label}
                    disabled={disabled}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

Tab.defaultProps = {
    className: '',
    label: 'Tab',
    disabled: false,
};

Tab.propTypes = {
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
     * disabled
     */
    disabled: PropTypes.bool,

    /**
     * onClick
     */
    onClick: PropTypes.any,

    /**
     * onKeyDown
     */
    onKeyDown: PropTypes.any,

    /**
     * renderButton
     */
    renderButton: PropTypes.any,

    /**
     * renderIcon
     */
    renderIcon: PropTypes.any,

    /**
     * secondaryLabel
     */
    secondaryLabel: PropTypes.any,

    /**
     * label
     */
    label: PropTypes.node,

};
