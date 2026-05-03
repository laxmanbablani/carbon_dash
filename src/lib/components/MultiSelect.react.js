import React from 'react';
import PropTypes from 'prop-types';
import { MultiSelect as CarbonMultiSelect } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const MultiSelect = (props) => {
    const { id, children, className = '', style = {}, loading_state, items = [], selectedItems = [], ...others } = props;

    const handleChange = ({ selectedItems: sel }) => {
        if (props.setProps) props.setProps({ selectedItems: sel || [] });
    };

    return (
        <CarbonMultiSelect
            id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            items={items} selectedItems={selectedItems}
            onChange={handleChange}
            {...others}
        >
            {children}
        </CarbonMultiSelect>
    );
};

MultiSelect.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func,
    children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    items: PropTypes.array,
    selectedItems: PropTypes.array,
    label: PropTypes.node, helperText: PropTypes.node, titleText: PropTypes.node,
    disabled: PropTypes.bool, invalid: PropTypes.bool, invalidText: PropTypes.node,
    warn: PropTypes.bool, warnText: PropTypes.node, size: PropTypes.oneOf(['sm','md','lg']),
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local','session','memory']),
};

MultiSelect.defaultProps = { items: [], selectedItems: [], disabled: false, size: 'md' };

export default MultiSelect;
