import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Dropdown is a wrapper for the Carbon Dropdown component.
 */
export default class Dropdown extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { selectedItem } = this.props;
        const { items } = this.props;
        const { label } = this.props;
        const { title } = this.props;

        const RealComponent = LazyLoader['Dropdown'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    selectedItem={selectedItem}
                    items={items}
                    label={label}
                    title={title}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

Dropdown.defaultProps = {
    className: '',
    selectedItem: null,
    items: [],
    label: 'Dropdown',
    title: 'Dropdown Title',
};

Dropdown.propTypes = {
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
     * helperText
     */
    helperText: PropTypes.any,

    /**
     * hideLabel
     */
    hideLabel: PropTypes.any,

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
    items: PropTypes.array,

    /**
     * label
     */
    label: PropTypes.string,

    /**
     * light
     */
    light: PropTypes.any,

    /**
     * onChange
     */
    onChange: PropTypes.any,

    /**
     * readOnly
     */
    readOnly: PropTypes.any,

    /**
     * renderSelectedItem
     */
    renderSelectedItem: PropTypes.any,

    /**
     * selectedItem
     */
    selectedItem: PropTypes.any,

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
     * type
     */
    type: PropTypes.any,

    /**
     * warn
     */
    warn: PropTypes.any,

    /**
     * warnText
     */
    warnText: PropTypes.any,

    /**
     * title
     */
    title: PropTypes.string,

};
