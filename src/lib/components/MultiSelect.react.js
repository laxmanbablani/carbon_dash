import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * MultiSelect is a wrapper for the Carbon MultiSelect component.
 */
export default class MultiSelect extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['MultiSelect'];
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

MultiSelect.defaultProps = {
    className: '',
};

MultiSelect.propTypes = {
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
     * compareItems
     */
    compareItems: PropTypes.any,

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
     * helperText
     */
    helperText: PropTypes.any,

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
     * label
     */
    label: PropTypes.any,

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
     * onMenuChange
     */
    onMenuChange: PropTypes.any,

    /**
     * open
     */
    open: PropTypes.any,

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
     * size
     */
    size: PropTypes.any,

    /**
     * slug
     */
    slug: PropTypes.any,

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

};
