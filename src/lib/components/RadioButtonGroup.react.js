import React from 'react';
import PropTypes from 'prop-types';
import { RadioButtonGroup as CarbonRadioButtonGroup } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const RadioButtonGroup = (props) => {
    const { id, children, className = '', style = {}, loading_state, value, ...others } = props;
    const handleChange = (e) => { if (props.setProps) props.setProps({ value: e?.target?.value ?? e ?? arguments[0] }); };
    return <CarbonRadioButtonGroup id={id} className={className} style={style} value={value} onChange={handleChange} data-dash-is-loading={getLoadingState(loading_state) || undefined} {...others}>{children}</CarbonRadioButtonGroup>;
};
RadioButtonGroup.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func, children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    value: PropTypes.string, defaultValue: PropTypes.string, labelText: PropTypes.node, helperText: PropTypes.node, legendText: PropTypes.node,
    disabled: PropTypes.bool, orientation: PropTypes.oneOf(['horizontal','vertical']), hideLabel: PropTypes.bool,
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string), persistence_type: PropTypes.oneOf(['local','session','memory']),
};
RadioButtonGroup.defaultProps = { disabled: false, orientation: 'horizontal' };
export default RadioButtonGroup;
