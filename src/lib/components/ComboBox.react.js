import React from 'react';
import PropTypes from 'prop-types';
import { ComboBox as CarbonComboBox } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * ComboBox is a dropdown with autocomplete functionality.
 * Wraps the Carbon ComboBox component.
 */
const ComboBox = (props) => {
    const {
        id,
        setProps,
        children,
        className = '',
        style = {},
        loading_state,
        items = [],
        selectedItem,
        ...others
    } = props;

    const handleChange = ({ selectedItem: item }) => {
        if (setProps) {
            setProps({ selectedItem: item });
        }
    };

    return (
        <CarbonComboBox
            id={id}
            className={className}
            style={style}
            items={items}
            selectedItem={selectedItem}
            onChange={handleChange}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonComboBox>
    );
};

ComboBox.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Dash-assigned callback for reactivity.
     */
    setProps: PropTypes.func,

    /**
     * Children elements (typically Text components for options, or custom renderers).
     */
    children: PropTypes.node,

    /**
     * Specify a custom className to be applied to the component.
     */
    className: PropTypes.string,

    /**
     * Inline styles.
     */
    style: PropTypes.object,

    /**
     * Dash loading state.
     */
    loading_state: PropTypes.shape({
        is_loading: PropTypes.bool,
        prop_name: PropTypes.string,
        component_name: PropTypes.string,
    }),

    /**
     * Array of items to display in the combobox.
     * Each item should have an id, text, and optionally disabled/icon properties.
     */
    items: PropTypes.array,

    /**
     * The currently selected item.
     */
    selectedItem: PropTypes.any,

    /**
     * Label text displayed above the combobox.
     */
    labelText: PropTypes.node,

    /**
     * Title text for the combobox (shown as help text/tooltip).
     */
    titleText: PropTypes.node,

    /**
     * Helper text displayed below the combobox.
     */
    helperText: PropTypes.node,

    /**
     * Placeholder text when no value is selected.
     */
    placeholder: PropTypes.string,

    /**
     * Whether the combobox is disabled.
     */
    disabled: PropTypes.bool,

    /**
     * Whether the combobox is in an invalid state.
     */
    invalid: PropTypes.bool,

    /**
     * Error message to display when invalid.
     */
    invalidText: PropTypes.node,

    /**
     * Whether the combobox is in a warning state.
     */
    warn: PropTypes.bool,

    /**
     * Warning message to display.
     */
    warnText: PropTypes.node,

    /**
     * Whether to allow custom values not in the items list.
     */
    allowCustomValue: PropTypes.bool,

    /**
     * Size of the combobox.
     */
    size: PropTypes.oneOf(['sm', 'md', 'lg']),

    /**
     * Light variant.
     */
    light: PropTypes.bool,

    /**
     * Direction of the dropdown menu.
     */
    direction: PropTypes.oneOf(['top', 'bottom']),

    /**
     * Used to allow user interactions in this component to be persisted.
     */
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),

    /**
     * Properties whose user interactions will persist.
     */
    persisted_props: PropTypes.arrayOf(PropTypes.string),

    /**
     * Where persisted user changes will be stored.
     */
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

ComboBox.defaultProps = {
    items: [],
    disabled: false,
    invalid: false,
    warn: false,
    allowCustomValue: false,
    size: 'md',
    light: false,
    direction: 'bottom',
};

export default ComboBox;
