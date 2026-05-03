import React from 'react';
import PropTypes from 'prop-types';
import { FluidNumberInput as CarbonFluidNumberInput, FluidNumberInputSkeleton as CarbonFluidNumberInputSkeleton } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * FluidNumberInput is a full-width number input component.
 */
const FluidNumberInput = (props) => {
    const {
        id,
        children,
        className = '',
        style = {},
        loading_state,
        value,
        labelText,
        helperText,
        invalid,
        invalidText,
        warn,
        warnText,
        disabled = false,
        hideLabel = false,
        ...others
    } = props;

    const handleChange = (e) => {
        if (props.setProps) {
            const target = e && e.target;
            props.setProps({ value: target ? target.value : e });
        }
    };

    if (loading_state && loading_state.is_loading) {
        return <CarbonFluidNumberInputSkeleton id={id} className={className} />;
    }

    return (
        <CarbonFluidNumberInput
            id={id}
            className={className}
            style={style}
            value={value}
            labelText={labelText}
            helperText={helperText}
            invalid={invalid}
            invalidText={invalidText}
            warn={warn}
            warnText={warnText}
            disabled={disabled}
            hideLabel={hideLabel}
            onChange={handleChange}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonFluidNumberInput>
    );
};

FluidNumberInput.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

    /** Dash callback to update props */
    setProps: PropTypes.func,

    /** The content of the number input */
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

    /** The value of the number input */
    value: PropTypes.number,

    /** Provide text that is used alongside the control label for additional help */
    labelText: PropTypes.node,

    /** Provide text that is used alongside the control label for additional help */
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

    /** Hide the label */
    hideLabel: PropTypes.bool,

    /** Specify the size of the number input */
    size: PropTypes.oneOf(['sm', 'md', 'lg']),

    /** Min value */
    min: PropTypes.number,

    /** Max value */
    max: PropTypes.number,

    /** Step value */
    step: PropTypes.number,

    /** Persistence settings */
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

FluidNumberInput.defaultProps = {
    disabled: false,
    invalid: false,
    warn: false,
    hideLabel: false,
    size: 'md',
    min: 0,
    max: 100,
    step: 1,
};

export default FluidNumberInput;