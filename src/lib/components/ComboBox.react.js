import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * ComboBox is a wrapper for the Carbon ComboBox component.
 */
export default class ComboBox extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['ComboBox'];
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

ComboBox.defaultProps = {
    className: '',
};

ComboBox.propTypes = {
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
     * allowCustomValue
     */
    allowCustomValue: PropTypes.any,

    /**
     * ariaLabel
     */
    ariaLabel: PropTypes.any,

    /**
     * autoAlign
     */
    autoAlign: PropTypes.any,

    /**
     * decorator
     */
    decorator: PropTypes.any,

    /**
     * direction
     */
    direction: PropTypes.any,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * downshiftProps
     */
    downshiftProps: PropTypes.any,

    /**
     * downshiftActions
     */
    downshiftActions: PropTypes.any,

    /**
     * helperText
     */
    helperText: PropTypes.any,

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
     * light
     */
    light: PropTypes.any,

    /**
     * onChange
     */
    onChange: PropTypes.any,

    /**
     * onInputChange
     */
    onInputChange: PropTypes.any,

    /**
     * onToggleClick
     */
    onToggleClick: PropTypes.any,

    /**
     * placeholder
     */
    placeholder: PropTypes.any,

    /**
     * readOnly
     */
    readOnly: PropTypes.any,

    /**
     * selectedItem
     */
    selectedItem: PropTypes.any,

    /**
     * shouldFilterItem
     */
    shouldFilterItem: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

    /**
     * slug
     */
    slug: PropTypes.any,

    /**
     * titleText
     */
    titleText: PropTypes.any,

    /**
     * translateWithId
     */
    translateWithId: PropTypes.any,

    /**
     * typeahead
     */
    typeahead: PropTypes.any,

    /**
     * warn
     */
    warn: PropTypes.any,

    /**
     * warnText
     */
    warnText: PropTypes.any,

    /**
     * inputProps
     */
    inputProps: PropTypes.any,

};
