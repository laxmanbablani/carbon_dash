import React from 'react';
import PropTypes from 'prop-types';
import { PasswordInput as CarbonPasswordInput } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const PasswordInput = (props) => {
    const { id, children, className = '', style = {}, loading_state, value, ...others } = props;
    const handleChange = (e) => { if (props.setProps) props.setProps({ value: e.target?.value ?? e }); };
    return <CarbonPasswordInput id={id} className={className} style={style} value={value} onChange={handleChange} data-dash-is-loading={getLoadingState(loading_state) || undefined} {...others}>{children}</CarbonPasswordInput>;
};
PasswordInput.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func, children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    value: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
    labelText: PropTypes.node, helperText: PropTypes.node, placeholder: PropTypes.string,
    disabled: PropTypes.bool, invalid: PropTypes.bool, invalidText: PropTypes.node,
    hideLabel: PropTypes.bool, hidePasswordLabel: PropTypes.string, showPasswordLabel: PropTypes.string,
    size: PropTypes.oneOf(['sm','md','lg']), light: PropTypes.bool, tooltipPosition: PropTypes.string,
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string), persistence_type: PropTypes.oneOf(['local','session','memory']),
};
PasswordInput.defaultProps = { disabled: false, invalid: false, hideLabel: false, size: 'md' };
export default PasswordInput;
