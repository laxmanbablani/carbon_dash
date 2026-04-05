import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * FluidMultiSelect is a wrapper for the Carbon FluidMultiSelect component.
 */
export default class FluidMultiSelect extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['FluidMultiSelect'];
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

FluidMultiSelect.defaultProps = {
    className: '',
};

FluidMultiSelect.propTypes = {
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
     * clearSelectionDescription
     */
    clearSelectionDescription: PropTypes.any,

    /**
     * clearSelectionText
     */
    clearSelectionText: PropTypes.any,

    /**
     * compareItems
     */
    compareItems: PropTypes.any,

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
     * isCondensed
     */
    isCondensed: PropTypes.any,

    /**
     * isFilterable
     */
    isFilterable: PropTypes.any,

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
     * readOnly
     */
    readOnly: PropTypes.any,

    /**
     * selectedItems
     */
    selectedItems: PropTypes.any,

    /**
     * selectionFeedback
     */
    selectionFeedback: PropTypes.any,

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

};
