import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * FluidSearch is a wrapper for the Carbon FluidSearch component.
 */
export default class FluidSearch extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['FluidSearch'];
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

FluidSearch.defaultProps = {
    className: '',
};

FluidSearch.propTypes = {
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

    /** persistence */
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),

    /** persisted_props */
    persisted_props: PropTypes.arrayOf(PropTypes.string),

    /** persistence_type */
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),

    /** n_blur */
    n_blur: PropTypes.number,

    /** n_submit */
    n_submit: PropTypes.number,

    /** debounce */
    debounce: PropTypes.oneOfType([PropTypes.bool, PropTypes.number]),

    /**
     * autoComplete
     */
    autoComplete: PropTypes.any,

    /**
     * closeButtonLabelText
     */
    closeButtonLabelText: PropTypes.any,

    /**
     * defaultValue
     */
    defaultValue: PropTypes.any,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * labelText
     */
    labelText: PropTypes.any,

    /**
     * onClear
     */
    onClear: PropTypes.any,

    /**
     * onKeyDown
     */
    onKeyDown: PropTypes.any,

    /**
     * placeholder
     */
    placeholder: PropTypes.any,

    /**
     * role
     */
    role: PropTypes.any,

    /**
     * type
     */
    type: PropTypes.any,

    /**
     * value
     */
    value: PropTypes.any,

    /**
     * onChange
     */
    onChange: PropTypes.any,

};
