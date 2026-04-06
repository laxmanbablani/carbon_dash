import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * FilterableMultiSelect is a wrapper for the Carbon FilterableMultiSelect component.
 */
export default class FilterableMultiSelect extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { open } = this.props;

        const RealComponent = LazyLoader['FilterableMultiSelect'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    open={open}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

FilterableMultiSelect.defaultProps = {
    className: '',
    open: false,
};

FilterableMultiSelect.propTypes = {
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
     * autoAlign
     */
    autoAlign: PropTypes.any,

    /**
     * clearSelectionDescription
     */
    clearSelectionDescription: PropTypes.any,

    /**
     * clearSelectionText
     */
    clearSelectionText: PropTypes.any,

    /**
     * decorator
     */
    decorator: PropTypes.any,

    /**
     * filterItems
     */
    filterItems: PropTypes.any,

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
     * hideLabel
     */
    hideLabel: PropTypes.any,

    /**
     * initialSelectedItems
     */
    initialSelectedItems: PropTypes.any,

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
     * locale
     */
    locale: PropTypes.any,

    /**
     * onChange
     */
    onChange: PropTypes.any,

    /**
     * onInputValueChange
     */
    onInputValueChange: PropTypes.any,

    /**
     * onMenuChange
     */
    onMenuChange: PropTypes.any,

    /**
     * open
     */
    open: PropTypes.bool,

    /**
     * placeholder
     */
    placeholder: PropTypes.any,

    /**
     * selectionFeedback
     */
    selectionFeedback: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

    /**
     * slug
     */
    slug: PropTypes.any,

    /**
     * compareItems
     */
    compareItems: PropTypes.any,

    /**
     * sortItems
     */
    sortItems: PropTypes.any,

    /**
     * titleText
     */
    titleText: PropTypes.any,

    /**
     * translateWithId
     */
    translateWithId: PropTypes.any,

    /**
     * type
     */
    type: PropTypes.any,

    /**
     * useTitleInItem
     */
    useTitleInItem: PropTypes.any,

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
