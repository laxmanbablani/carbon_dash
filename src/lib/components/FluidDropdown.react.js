import React from 'react';
import PropTypes from 'prop-types';
import { FluidDropdown as CarbonFluidDropdown, FluidDropdownSkeleton as CarbonFluidDropdownSkeleton } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * FluidDropdown is a full-width Dropdown component.
 */
const FluidDropdown = (props) => {
    const {
        id,
        children,
        className = '',
        style = {},
        loading_state,
        items = [],
        selectedItem,
        label,
        titleText,
        helperText,
        invalid,
        invalidText,
        warn,
        warnText,
        disabled = false,
        ...others
    } = props;

    if (loading_state && loading_state.is_loading) {
        return <CarbonFluidDropdownSkeleton id={id} className={className} />;
    }

    const handleChange = ({ selectedItem: item }) => {
        if (props.setProps) {
            props.setProps({ selectedItem: item });
        }
    };

    return (
        <CarbonFluidDropdown
            id={id}
            className={className}
            style={style}
            items={items}
            selectedItem={selectedItem}
            label={label}
            titleText={titleText}
            helperText={helperText}
            invalid={invalid}
            invalidText={invalidText}
            warn={warn}
            warnText={warnText}
            disabled={disabled}
            onChange={handleChange}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonFluidDropdown>
    );
};

FluidDropdown.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

    /** Dash callback to update props */
    setProps: PropTypes.func,

    /** The content of the dropdown */
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

    /** The items to display in the dropdown */
    items: PropTypes.array,

    /** The selected item */
    selectedItem: PropTypes.any,

    /** Provide text that is used alongside the control label */
    label: PropTypes.node,

    /** Provide the title text for the dropdown */
    titleText: PropTypes.node,

    /** Provide text that is used alongside the control label */
    helperText: PropTypes.node,

    /** Specify whether the control is currently in an invalid state */
    invalid: PropTypes.bool,

    /** Provide the text that is displayed when the control is in an invalid state */
    invalidText: PropTypes.node,

    /** Specify whether the control is currently in a warning state */
    warn: PropTypes.bool,

    /** Provide the text that is displayed when the control is in a warning state */
    warnText: PropTypes.node,

    /** Specify whether the control is disabled */
    disabled: PropTypes.bool,

    /** Specify the size of the dropdown */
    size: PropTypes.oneOf(['sm', 'md', 'lg']),

    /** Persistence settings */
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

FluidDropdown.defaultProps = {
    items: [],
    disabled: false,
    invalid: false,
    warn: false,
    size: 'md',
};

export default FluidDropdown;