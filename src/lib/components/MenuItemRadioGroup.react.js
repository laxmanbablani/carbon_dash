import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * MenuItemRadioGroup is a wrapper for the Carbon MenuItemRadioGroup component.
 */
export default class MenuItemRadioGroup extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { selectedItem } = this.props;

        const RealComponent = LazyLoader['MenuItemRadioGroup'];
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

MenuItemRadioGroup.defaultProps = {
    className: '',
    selectedItem: null,
};

MenuItemRadioGroup.propTypes = {
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
     * defaultSelectedItem
     */
    defaultSelectedItem: PropTypes.any,

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

};
