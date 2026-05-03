import React from 'react';
import PropTypes from 'prop-types';
import { Toggle as CarbonToggle, ToggleSkeleton as CarbonToggleSkeleton } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const Toggle = (props) => {
    const { id, children, className = '', style = {}, loading_state, toggled = false, ...others } = props;

    if (loading_state && loading_state.is_loading) {
        return <CarbonToggleSkeleton id={id} className={className} />;
    }

    const handleToggle = (e) => {
        if (props.setProps) props.setProps({ toggled: e?.target?.checked ?? e?.checked ?? !toggled });
    };

    return (
        <CarbonToggle
            id={id}
            className={className}
            style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            toggled={toggled}
            onChange={handleToggle}
            {...others}
        >
            {children}
        </CarbonToggle>
    );
};

Toggle.propTypes = {
    id: PropTypes.string,
    setProps: PropTypes.func,
    children: PropTypes.node,
    className: PropTypes.string,
    style: PropTypes.object,
    loading_state: PropTypes.shape({
        is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string,
    }),
    /** Toggle label text */
    labelText: PropTypes.node,
    /** Label for A (off) position */
    labelA: PropTypes.node,
    /** Label for B (on) position */
    labelB: PropTypes.node,
    /** Whether the toggle is on */
    toggled: PropTypes.bool,
    /** Whether the toggle is disabled */
    disabled: PropTypes.bool,
    /** Size of the toggle */
    size: PropTypes.oneOf(['sm', 'md']),
    /** Whether to hide the label */
    hideLabel: PropTypes.bool,
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

Toggle.defaultProps = {
    toggled: false,
    disabled: false,
    size: 'md',
};

export default Toggle;
