import React from 'react';
import PropTypes from 'prop-types';
import { TimePickerSelect as CarbonTimePickerSelect } from '@carbon/react';

const TimePickerSelect = (props) => {
    const { id, children, className, style, loading_state, ...others } = props;
    return (
        <CarbonTimePickerSelect
            id={id} className={className} style={style}
            data-dash-is-loading={loading_state?.is_loading || undefined}
            {...others}
        >
            {children}
        </CarbonTimePickerSelect>
    );
};

TimePickerSelect.propTypes = {
    id: PropTypes.string, children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    /** Label text */
    labelText: PropTypes.node,
    /** Whether disabled */
    disabled: PropTypes.bool,
    /** Whether to hide label */
    hideLabel: PropTypes.bool,
};

export default TimePickerSelect;
