import React from 'react';
import PropTypes from 'prop-types';
import {
    TimePicker as CarbonTimePicker,
    TimePickerSelect as CarbonTimePickerSelect,
} from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const TimePicker = (props) => {
    const { id, children, className = '', style = {}, loading_state, value, ...others } = props;

    const handleChange = (e) => {
        if (props.setProps) props.setProps({ value: e.target?.value ?? e });
    };

    return (
        <CarbonTimePicker
            id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            value={value}
            onChange={handleChange}
            {...others}
        >
            {children}
        </CarbonTimePicker>
    );
};

TimePicker.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func,
    children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    /** Current time value */
    value: PropTypes.string,
    /** Label text */
    labelText: PropTypes.node,
    /** Placeholder */
    placeholder: PropTypes.string,
    /** Whether disabled */
    disabled: PropTypes.bool,
    /** Whether invalid */
    invalid: PropTypes.bool,
    /** Invalid text */
    invalidText: PropTypes.node,
    /** Size */
    size: PropTypes.oneOf(['sm', 'md', 'lg']),
    /** Light variant */
    light: PropTypes.bool,
    /** Hide label */
    hideLabel: PropTypes.bool,
    /** Whether readonly */
    readOnly: PropTypes.bool,
    /** Format pattern */
    pattern: PropTypes.string,
    /** Type */
    type: PropTypes.string,
    /** Time format: '12' or '24' */
    timeFormat: PropTypes.oneOf(['12', '24']),
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

TimePicker.defaultProps = { disabled: false, size: 'md', timeFormat: '12' };

export default TimePicker;
