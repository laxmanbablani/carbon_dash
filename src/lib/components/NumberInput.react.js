import React from 'react';
import PropTypes from 'prop-types';
import {
    NumberInput as CarbonNumberInput,
    NumberInputSkeleton as CarbonNumberInputSkeleton,
} from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const NumberInput = (props) => {
    const { id, children, className = '', style = {}, loading_state, value, ...others } = props;

    if (loading_state && loading_state.is_loading) {
        return <CarbonNumberInputSkeleton id={id} className={className} />;
    }

    const handleChange = (e) => {
        const val = e?.target?.value ?? e?.implicit_value ?? e;
        if (props.setProps) props.setProps({ value: val });
    };

    return (
        <CarbonNumberInput
            id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            value={value}
            onChange={handleChange}
            {...others}
        />
    );
};

NumberInput.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func,
    children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    /** The value */
    value: PropTypes.oneOfType([PropTypes.number, PropTypes.string]),
    /** Label text */
    label: PropTypes.node,
    /** Helper text */
    helperText: PropTypes.node,
    /** Minimum value */
    min: PropTypes.number,
    /** Maximum value */
    max: PropTypes.number,
    /** Step value */
    step: PropTypes.number,
    /** Whether disabled */
    disabled: PropTypes.bool,
    /** Whether readonly */
    readOnly: PropTypes.bool,
    /** Whether invalid */
    invalid: PropTypes.bool,
    /** Invalid text */
    invalidText: PropTypes.node,
    /** Whether warn */
    warn: PropTypes.bool,
    /** Warn text */
    warnText: PropTypes.node,
    /** Size */
    size: PropTypes.oneOf(['sm', 'md', 'lg']),
    /** Whether to hide steppers with mouse event */
    hideSteppers: PropTypes.bool,
    /** Whether to hide label */
    hideLabel: PropTypes.bool,
    /** Whether lightweight */
    light: PropTypes.bool,
    /** Allow empty value */
    allowEmpty: PropTypes.bool,
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

NumberInput.defaultProps = {
    disabled: false, invalid: false, warn: false, hideLabel: false,
    hideSteppers: false, size: 'md', allowEmpty: false,
    min: 0, max: 100, step: 1,
};

export default NumberInput;
