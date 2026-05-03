import React from 'react';
import PropTypes from 'prop-types';
import { FluidDatePicker as CarbonFluidDatePicker, FluidDatePickerSkeleton as CarbonFluidDatePickerSkeleton } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * FluidDatePicker is a full-width DatePicker component.
 */
const FluidDatePicker = (props) => {
    const {
        id,
        children,
        className = '',
        style = {},
        loading_state,
        datePickerType = 'simple',
        ...others
    } = props;

    if (loading_state && loading_state.is_loading) {
        return <CarbonFluidDatePickerSkeleton id={id} className={className} datePickerType={datePickerType} />;
    }

    return (
        <CarbonFluidDatePicker
            id={id}
            className={className}
            style={style}
            datePickerType={datePickerType}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonFluidDatePicker>
    );
};

FluidDatePicker.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

    /** Dash callback to update props */
    setProps: PropTypes.func,

    /** The content of the date picker (DatePickerInput components) */
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

    /** Specify the type of date picker */
    datePickerType: PropTypes.oneOf(['simple', 'single', 'range']),

    /** Callback for date change */
    onChange: PropTypes.func,

    /** Persistence settings */
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

FluidDatePicker.defaultProps = {
    datePickerType: 'simple',
};

export default FluidDatePicker;