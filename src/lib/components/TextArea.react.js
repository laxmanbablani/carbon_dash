import React from 'react';
import PropTypes from 'prop-types';
import { TextArea as CarbonTextArea, TextAreaSkeleton as CarbonSkeleton } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const TextArea = (props) => {
    const { id, children, className = '', style = {}, loading_state, value, rows = 4, cols = 50, ...others } = props;
    if (loading_state && loading_state.is_loading) return <CarbonSkeleton id={id} className={className} />;
    const handleChange = (e) => { if (props.setProps) props.setProps({ value: e.target?.value ?? e }); };
    return <CarbonTextArea id={id} className={className} style={style} value={value} rows={rows} cols={cols} onChange={handleChange} data-dash-is-loading={getLoadingState(loading_state) || undefined} {...others}>{children}</CarbonTextArea>;
};
TextArea.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func, children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    value: PropTypes.string, labelText: PropTypes.node, helperText: PropTypes.node, placeholder: PropTypes.string,
    rows: PropTypes.number, cols: PropTypes.number, disabled: PropTypes.bool, readOnly: PropTypes.bool,
    invalid: PropTypes.bool, invalidText: PropTypes.node, warn: PropTypes.bool, warnText: PropTypes.node,
    enableCounter: PropTypes.bool, maxCount: PropTypes.number, hideLabel: PropTypes.bool, size: PropTypes.oneOf(['sm','md','lg']),
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string), persistence_type: PropTypes.oneOf(['local','session','memory']),
};
TextArea.defaultProps = { disabled: false, rows: 4, cols: 50, size: 'md' };
export default TextArea;
