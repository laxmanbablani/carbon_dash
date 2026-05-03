import React from 'react';
import PropTypes from 'prop-types';
import { Dropdown as CarbonDropdown, DropdownSkeleton as CarbonDropdownSkeleton } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const Dropdown = (props) => {
    const { id, children, className = '', style = {}, loading_state, items, selectedItem, ...others } = props;

    if (loading_state && loading_state.is_loading) {
        return <CarbonDropdownSkeleton id={id} className={className} />;
    }

    const handleChange = ({ selectedItem: item }) => {
        if (props.setProps) props.setProps({ selectedItem: item });
    };

    return (
        <CarbonDropdown
            id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            items={items || []}
            selectedItem={selectedItem}
            onChange={handleChange}
            {...others}
        />
    );
};

Dropdown.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func, children: PropTypes.node,
    className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    /** List of items to show in the dropdown */
    items: PropTypes.array,
    /** Currently selected item */
    selectedItem: PropTypes.any,
    /** Label text displayed above */
    label: PropTypes.node,
    /** Title text */
    titleText: PropTypes.node,
    /** Helper text */
    helperText: PropTypes.node,
    /** Whether disabled */
    disabled: PropTypes.bool,
    /** Direction: top or bottom */
    direction: PropTypes.oneOf(['top', 'bottom']),
    /** Size */
    size: PropTypes.oneOf(['sm', 'md', 'lg']),
    /** Inline variant */
    inline: PropTypes.bool,
    /** Whether invalid */
    invalid: PropTypes.bool,
    /** Invalid text */
    invalidText: PropTypes.node,
    /** Whether warn */
    warn: PropTypes.bool,
    /** Warn text */
    warnText: PropTypes.node,
    /** Light variant */
    light: PropTypes.bool,
    /** Type: default or inline */
    type: PropTypes.oneOf(['default', 'inline']),
    /** Whether to show AI label decorator */
    decorator: PropTypes.node,
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

Dropdown.defaultProps = {
    items: [], disabled: false, invalid: false, warn: false,
    direction: 'bottom', size: 'md', inline: false,
    type: 'default',
};

export default Dropdown;
