import React from 'react';
import PropTypes from 'prop-types';
import { Tooltip as CarbonTooltip } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const Tooltip = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;
    return (
        <CarbonTooltip
            id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonTooltip>
    );
};

Tooltip.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func,
    children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    /** Tooltip trigger label */
    label: PropTypes.node,
    /** Tooltip description/content */
    description: PropTypes.node,
    /** Alignment relative to trigger */
    align: PropTypes.oneOf(['top', 'bottom', 'left', 'right', 'top-left', 'top-right', 'bottom-left', 'bottom-right']),
    /** Whether open by default */
    defaultOpen: PropTypes.bool,
    /** Whether to close on activation */
    closeOnActivation: PropTypes.bool,
    /** Delay before showing (ms) */
    enterDelayMs: PropTypes.number,
    /** Delay before hiding (ms) */
    leaveDelayMs: PropTypes.number,
    /** Whether to show a drop shadow */
    dropShadow: PropTypes.bool,
    /** High contrast variant */
    highContrast: PropTypes.bool,
    /** Auto-align to viewport */
    autoAlign: PropTypes.bool,
};

Tooltip.defaultProps = { defaultOpen: false, align: 'top', enterDelayMs: 100, leaveDelayMs: 300, dropShadow: false, highContrast: false, closeOnActivation: false };

export default Tooltip;
