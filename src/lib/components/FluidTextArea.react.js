import React from 'react';
import PropTypes from 'prop-types';
import { FluidTextArea as CarbonFluidTextArea, FluidTextAreaSkeleton as CarbonFluidTextAreaSkeleton } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * FluidTextArea is a full-width TextArea component.
 */
const FluidTextArea = (props) => {
    const {
        id,
        children,
        className = '',
        style = {},
        loading_state,
        value,
        labelText,
        placeholder,
        helperText,
        invalid,
        invalidText,
        warn,
        warnText,
        disabled = false,
        readOnly = false,
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
        return <CarbonFluidTextAreaSkeleton id={id} className={className} />;
    }

    return (
        <CarbonFluidTextArea
            id={id}
            className={className}
            style={style}
            value={value}
            labelText={labelText}
            placeholder={placeholder}
            helperText={helperText}
            invalid={invalid}
            invalidText={invalidText}
            warn={warn}
            warnText={warnText}
            disabled={disabled}
            readOnly={readOnly}
            hideLabel={hideLabel}
            onChange={handleChange}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonFluidTextArea>
    );
};

FluidTextArea.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

    /** Dash callback to update props */
    setProps: PropTypes.func,

    /** The content of the text area */
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

    /** The value of the text area */
    value: PropTypes.string,

    /** Provide text that is used alongside the control label for additional help */
    labelText: PropTypes.node,

    /** Provide the placeholder text for the text area */
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

    /** Specify whether the control is read-only */
    readOnly: PropTypes.bool,

    /** Hide the label */
    hideLabel: PropTypes.bool,

    /** Specify the number of rows */
    rows: PropTypes.number,

    /** Specify the number of cols */
    cols: PropTypes.number,

    /** Enable the counter */
    enableCounter: PropTypes.bool,

    /** Max count for the counter */
    maxCount: PropTypes.number,

    /** Persistence settings */
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

FluidTextArea.defaultProps = {
    disabled: false,
    readOnly: false,
    hideLabel: false,
    rows: 4,
    cols: 50,
    enableCounter: false,
};

export default FluidTextArea;