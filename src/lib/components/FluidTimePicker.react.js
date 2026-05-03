import React from 'react';
import PropTypes from 'prop-types';
import { FluidTimePicker as CarbonFluidTimePicker, FluidTimePickerSelect as CarbonFluidTimePickerSelect } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * FluidTimePicker is a full-width TimePicker component.
 */
const FluidTimePicker = (props) => {
    const {
        id,
        children,
        className = '',
        style = {},
        loading_state,
        labelText,
        ...others
    } = props;

    if (loading_state && loading_state.is_loading) {
        return <CarbonFluidTimePicker className={className} disabled />;
    }

    return (
        <CarbonFluidTimePicker
            id={id}
            className={className}
            style={style}
            labelText={labelText}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonFluidTimePicker>
    );
};

FluidTimePicker.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

    /** Dash callback to update props */
    setProps: PropTypes.func,

    /** The content of the time picker (FluidTimePickerSelect components) */
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

    /** Provide text that is used alongside the control label for additional help */
    labelText: PropTypes.node,

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

    /** Persistence settings */
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

FluidTimePicker.defaultProps = {
    disabled: false,
    invalid: false,
    warn: false,
};

export default FluidTimePicker;