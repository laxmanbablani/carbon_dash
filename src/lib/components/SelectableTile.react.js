import React from 'react';
import PropTypes from 'prop-types';
import { SelectableTile as CarbonSelectableTile } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const SelectableTile = (props) => {
    const { id, children, className = '', style = {}, loading_state, selected = false, ...others } = props;

    const handleChange = (e) => {
        if (props.setProps) props.setProps({ selected: e?.target?.checked ?? !selected });
    };

    return (
        <CarbonSelectableTile
            id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            selected={selected}
            onChange={handleChange}
            {...others}
        >
            {children}
        </CarbonSelectableTile>
    );
};

SelectableTile.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func,
    children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    /** Whether the tile is selected */
    selected: PropTypes.bool,
    /** Value associated with this tile */
    value: PropTypes.string,
    /** Whether disabled */
    disabled: PropTypes.bool,
    /** Title text for accessibility */
    title: PropTypes.string,
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

SelectableTile.defaultProps = { selected: false, disabled: false };

export default SelectableTile;
