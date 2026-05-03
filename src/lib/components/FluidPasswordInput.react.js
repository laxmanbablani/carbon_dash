import React from 'react';
import PropTypes from 'prop-types';
import { FluidPasswordInput as CarbonFluidPasswordInput } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * FluidPasswordInput is a full-width password input component.
 */
const FluidPasswordInput = (props) => {
    const {
        id,
        children,
        className = '',
        style = {},
        loading_state,
        labelText,
        placeholder,
        helperText,
        invalid,
        invalidText,
        warn,
        warnText,
        disabled = false,
        hideLabel = false,
        ...others
    } = props;

    if (loading_state && loading_state.is_loading) {
        return <CarbonFluidPasswordInput className={className} disabled />;
    }

    return (
        <CarbonFluidPasswordInput
            id={id}
            className={className}
            style={style}
            labelText={labelText}
            placeholder={placeholder}
            helperText={helperText}
            invalid={invalid}
            invalidText={invalidText}
            warn={warn}
            warnText={warnText}
            disabled={disabled}
            hideLabel={hideLabel}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonFluidPasswordInput>
    );
};

FluidPasswordInput.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

    /** Dash callback to update props */
    setProps: PropTypes.func,

    /** The content of the password input */
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

    /** Provide the placeholder text for the password input */
    placeholder: PropTypes.string,

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

    /** Persistence settings */
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

FluidPasswordInput.defaultProps = {
    disabled: false,
    hideLabel: false,
};

export default FluidPasswordInput;