import React from 'react';
import PropTypes from 'prop-types';
import { Checkbox as CarbonCheckbox, CheckboxSkeleton as CarbonCheckboxSkeleton } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const Checkbox = (props) => {
    const { id, children, className = '', style = {}, loading_state, checked = false, ...others } = props;

    if (loading_state && loading_state.is_loading) {
        return <CarbonCheckboxSkeleton id={id} className={className} />;
    }

    const handleChange = (e) => {
        if (props.setProps) props.setProps({ checked: e?.checked ?? e?.target?.checked });
    };

    return (
        <CarbonCheckbox
            id={id}
            className={className}
            style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            checked={checked}
            onChange={handleChange}
            {...others}
        >
            {children}
        </CarbonCheckbox>
    );
};

Checkbox.propTypes = {
    id: PropTypes.string,
    setProps: PropTypes.func,
    children: PropTypes.node,
    className: PropTypes.string,
    style: PropTypes.object,
    loading_state: PropTypes.shape({
        is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string,
    }),
    /** Checkbox label text */
    labelText: PropTypes.node,
    /** Whether the checkbox is checked */
    checked: PropTypes.bool,
    /** Whether the checkbox is disabled */
    disabled: PropTypes.bool,
    /** Whether the checkbox is in an indeterminate state */
    indeterminate: PropTypes.bool,
    /** Whether to hide the label */
    hideLabel: PropTypes.bool,
    /** The value submitted with the form */
    value: PropTypes.string,
    /** Title attribute */
    title: PropTypes.string,
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

Checkbox.defaultProps = {
    checked: false,
    disabled: false,
    indeterminate: false,
    hideLabel: false,
};

export default Checkbox;
