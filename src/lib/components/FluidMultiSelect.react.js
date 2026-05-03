import React from 'react';
import PropTypes from 'prop-types';
import { FluidMultiSelect as CarbonFluidMultiSelect, FluidMultiSelectSkeleton as CarbonFluidMultiSelectSkeleton } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * FluidMultiSelect is a full-width MultiSelect component.
 */
const FluidMultiSelect = (props) => {
    const {
        id,
        children,
        className = '',
        style = {},
        loading_state,
        items = [],
        selectedItems,
        ...others
    } = props;

    if (loading_state && loading_state.is_loading) {
        return <CarbonFluidMultiSelectSkeleton id={id} className={className} />;
    }

    const handleChange = ({ selectedItems: items }) => {
        if (props.setProps) {
            props.setProps({ selectedItems: items });
        }
    };

    return (
        <CarbonFluidMultiSelect
            id={id}
            className={className}
            style={style}
            items={items}
            selectedItems={selectedItems}
            onChange={handleChange}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonFluidMultiSelect>
    );
};

FluidMultiSelect.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

    /** Dash callback to update props */
    setProps: PropTypes.func,

    /** The content of the multi select */
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

    /** The items to display in the multi select */
    items: PropTypes.array,

    /** The selected items */
    selectedItems: PropTypes.array,

    /** Provide text that is used alongside the control label */
    label: PropTypes.node,

    /** Provide the title text for the multi select */
    titleText: PropTypes.node,

    /** Provide text that is used alongside the control label */
    helperText: PropTypes.node,

    /** Provide the placeholder text */
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

    /** Specify the size of the multi select */
    size: PropTypes.oneOf(['sm', 'md', 'lg']),

    /** Persistence settings */
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

FluidMultiSelect.defaultProps = {
    items: [],
    disabled: false,
    invalid: false,
    warn: false,
    size: 'md',
};

export default FluidMultiSelect;