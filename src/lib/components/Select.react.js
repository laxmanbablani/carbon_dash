import React from 'react';
import PropTypes from 'prop-types';
import { Select as CarbonSelect, SelectSkeleton as CarbonSelectSkeleton } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const Select = (props) => {
    const { id, children, className = '', style = {}, loading_state, value, ...others } = props;

    if (loading_state && loading_state.is_loading) {
        return <CarbonSelectSkeleton id={id} className={className} />;
    }

    const handleChange = (e) => {
        if (props.setProps) props.setProps({ value: e.target?.value ?? e });
    };

    return (
        <CarbonSelect
            id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            value={value}
            onChange={handleChange}
            {...others}
        >
            {children}
        </CarbonSelect>
    );
};

Select.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func,
    children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    /** Current value of the select */
    value: PropTypes.any,
    /** Default value (uncontrolled) */
    defaultValue: PropTypes.any,
    /** Label text */
    labelText: PropTypes.node,
    /** Whether the select is disabled */
    disabled: PropTypes.bool,
    /** Whether the select is in invalid state */
    invalid: PropTypes.bool,
    /** Invalid state text */
    invalidText: PropTypes.node,
    /** Whether the select is in warning state */
    warn: PropTypes.bool,
    /** Warning state text */
    warnText: PropTypes.node,
    /** Helper text */
    helperText: PropTypes.node,
    /** Whether the label should be visually hidden */
    hideLabel: PropTypes.bool,
    /** Whether the label should be lightweight */
    light: PropTypes.bool,
    /** Size */
    size: PropTypes.oneOf(['sm', 'md', 'lg']),
    /** Inline variant */
    inline: PropTypes.bool,
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

Select.defaultProps = { disabled: false, invalid: false, warn: false, hideLabel: false, inline: false, size: 'md' };

export default Select;
