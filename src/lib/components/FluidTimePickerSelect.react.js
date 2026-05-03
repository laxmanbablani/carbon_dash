import React from 'react';
import PropTypes from 'prop-types';
import { TimePickerSelect as CarbonTimePickerSelect } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * FluidTimePickerSelect is a full-width TimePickerSelect component.
 */
const FluidTimePickerSelect = (props) => {
    const {
        id,
        children,
        className = '',
        style = {},
        loading_state,
        labelText,
        ...others
    } = props;

    return (
        <CarbonTimePickerSelect
            id={id}
            className={className}
            style={style}
            labelText={labelText}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonTimePickerSelect>
    );
};

FluidTimePickerSelect.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

    /** Dash callback to update props */
    setProps: PropTypes.func,

    /** The content of the time picker select (SelectItem components) */
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

    /** Provide the label text for the time picker select */
    labelText: PropTypes.node,

    /** Specify whether the control is disabled */
    disabled: PropTypes.bool,

    /** Persistence settings */
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

FluidTimePickerSelect.defaultProps = {
    disabled: false,
};

export default FluidTimePickerSelect;