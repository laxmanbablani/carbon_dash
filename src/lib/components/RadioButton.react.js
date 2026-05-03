import React from 'react';
import PropTypes from 'prop-types';
import { RadioButton as CarbonRadioButton } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const RadioButton = (props) => {
    const { id, children, className = '', style = {}, loading_state, checked = false, ...others } = props;
    const handleChange = (e) => { if (props.setProps) props.setProps({ checked: e?.target?.checked ?? !checked }); };
    return <CarbonRadioButton id={id} className={className} style={style} checked={checked} onChange={handleChange} data-dash-is-loading={getLoadingState(loading_state) || undefined} {...others}>{children}</CarbonRadioButton>;
};
RadioButton.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func, children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    checked: PropTypes.bool, labelText: PropTypes.node, disabled: PropTypes.bool, hideLabel: PropTypes.bool, value: PropTypes.string,
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string), persistence_type: PropTypes.oneOf(['local','session','memory']),
};
RadioButton.defaultProps = { checked: false, disabled: false };
export default RadioButton;
