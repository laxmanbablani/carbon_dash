import React from 'react';
import PropTypes from 'prop-types';
import { OverflowMenu as CarbonOverflowMenu } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const OverflowMenu = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;
    return (
        <CarbonOverflowMenu id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined} {...others}>
            {children}
        </CarbonOverflowMenu>
    );
};

OverflowMenu.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func,
    children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    flipped: PropTypes.bool, ariaLabel: PropTypes.string,
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local','session','memory']),
};

OverflowMenu.defaultProps = { flipped: false };
export default OverflowMenu;
