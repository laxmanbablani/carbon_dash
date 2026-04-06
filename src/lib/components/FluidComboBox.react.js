import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * FluidComboBox is a wrapper for the Carbon FluidComboBox component.
 */
export default class FluidComboBox extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { selectedItem } = this.props;

        const RealComponent = LazyLoader['FluidComboBox'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    selectedItem={selectedItem}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

FluidComboBox.defaultProps = {
    className: '',
    selectedItem: null,
};

FluidComboBox.propTypes = {
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
     * direction
     */
    direction: PropTypes.any,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * initialSelectedItem
     */
    initialSelectedItem: PropTypes.any,

    /**
     * invalid
     */
    invalid: PropTypes.any,

    /**
     * invalidText
     */
    invalidText: PropTypes.any,

    /**
     * isCondensed
     */
    isCondensed: PropTypes.any,

    /**
     * itemToElement
     */
    itemToElement: PropTypes.any,

    /**
     * itemToString
     */
    itemToString: PropTypes.any,

    /**
     * items
     */
    items: PropTypes.any,

    /**
     * label
     */
    label: PropTypes.any,

    /**
     * onChange
     */
    onChange: PropTypes.any,

    /**
     * selectedItem
     */
    selectedItem: PropTypes.any,

    /**
     * titleText
     */
    titleText: PropTypes.any,

    /**
     * translateWithId
     */
    translateWithId: PropTypes.any,

    /**
     * warn
     */
    warn: PropTypes.any,

    /**
     * warnText
     */
    warnText: PropTypes.any,

};
