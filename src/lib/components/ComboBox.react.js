import React from 'react';
import PropTypes from 'prop-types';
import { ComboBox as CarbonComboBox, ComboBoxSkeleton as CarbonComboBoxSkeleton } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const ComboBox = (props) => {
    const { id, children, className = '', style = {}, loading_state, items = [], selectedItem, ...others } = props;
    if (loading_state && loading_state.is_loading) return <CarbonComboBoxSkeleton id={id} className={className} />;
    const handleChange = ({ selectedItem: item }) => { if (props.setProps) props.setProps({ selectedItem: item }); };
    return <CarbonComboBox id={id} className={className} style={style} items={items} selectedItem={selectedItem} onChange={handleChange} data-dash-is-loading={getLoadingState(loading_state) || undefined} {...others}>{children}</CarbonComboBox>;
};
ComboBox.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func, children: PropTypes.node,
    className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    items: PropTypes.array, selectedItem: PropTypes.any,
    labelText: PropTypes.node, titleText: PropTypes.node, helperText: PropTypes.node, placeholder: PropTypes.string,
    disabled: PropTypes.bool, invalid: PropTypes.bool, invalidText: PropTypes.node, warn: PropTypes.bool, warnText: PropTypes.node,
    allowCustomValue: PropTypes.bool, size: PropTypes.oneOf(['sm','md','lg']), light: PropTypes.bool, direction: PropTypes.oneOf(['top','bottom']),
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string), persistence_type: PropTypes.oneOf(['local','session','memory']),
};
ComboBox.defaultProps = { items: [], disabled: false, invalid: false, warn: false, size: 'md', allowCustomValue: false, direction: 'bottom' };
export default ComboBox;
