import React from 'react';
import PropTypes from 'prop-types';
import { FluidComboBox as CarbonFluidComboBox, FluidComboBoxSkeleton as CarbonFluidComboBoxSkeleton } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * FluidComboBox is a full-width ComboBox component.
 */
const FluidComboBox = (props) => {
    const {
        id,
        children,
        className = '',
        style = {},
        loading_state,
        items = [],
        selectedItem,
        ...others
    } = props;

    if (loading_state && loading_state.is_loading) {
        return <CarbonFluidComboBoxSkeleton id={id} className={className} />;
    }

    const handleChange = ({ selectedItem: item }) => {
        if (props.setProps) {
            props.setProps({ selectedItem: item });
        }
    };

    return (
        <CarbonFluidComboBox
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
        </CarbonFluidComboBox>
    );
};

FluidComboBox.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

    /** Dash callback to update props */
    setProps: PropTypes.func,

    /** The content of the combo box */
    children: PropTypes.node,

    /** Custom CSS class */
    className: PropTypes.string,

    /** Inline styles */
    style: PropTypes.object,

    /** Dash loading state */
    loading_state: PropTypes.shape({
        is_loading: PropTypes.bool,
        prop_name: PropTypes.string,
        component_name: PropTypes.string,
    }),

    /** The items to display in the combo box */
    items: PropTypes.array,

    /** The selected item */
    selectedItem: PropTypes.any,

    /** Provide text that is used alongside the control label */
    labelText: PropTypes.node,

    /** Provide the title text for the combo box */
    titleText: PropTypes.node,

    /** Provide text that is used alongside the control label */
    helperText: PropTypes.node,

    /** Provide the placeholder text for the combo box */
    placeholder: PropTypes.string,

    /** Specify whether the control is disabled */
    disabled: PropTypes.bool,

    /** Specify whether the control is in an invalid state */
    invalid: PropTypes.bool,

    /** Provide the text that is displayed when the control is in an invalid state */
    invalidText: PropTypes.node,

    /** Specify whether the control is in a warning state */
    warn: PropTypes.bool,

    /** Provide the text that is displayed when the control is in a warning state */
    warnText: PropTypes.node,

    /** Allow custom values not in the list */
    allowCustomValue: PropTypes.bool,

    /** Specify the size of the combo box */
    size: PropTypes.oneOf(['sm', 'md', 'lg']),

    /** Specify the direction of the dropdown */
    direction: PropTypes.oneOf(['top', 'bottom']),

    /** Persistence settings */
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

FluidComboBox.defaultProps = {
    items: [],
    disabled: false,
    invalid: false,
    warn: false,
    size: 'md',
    allowCustomValue: false,
    direction: 'bottom',
};

export default FluidComboBox;