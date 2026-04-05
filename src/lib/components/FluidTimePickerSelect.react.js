import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * FluidTimePickerSelect is a wrapper for the Carbon FluidTimePickerSelect component.
 */
export default class FluidTimePickerSelect extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['FluidTimePickerSelect'];
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

FluidTimePickerSelect.defaultProps = {
    className: '',
};

FluidTimePickerSelect.propTypes = {
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
     * onChange
     */
    onChange: PropTypes.any,

};
