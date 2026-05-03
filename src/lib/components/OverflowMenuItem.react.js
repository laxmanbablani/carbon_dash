import React from 'react';
import PropTypes from 'prop-types';
import { OverflowMenuItem as CarbonOverflowMenuItem } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const OverflowMenuItem = (props) => {
    const { id, children, className = '', style = {}, loading_state, n_clicks = 0, ...others } = props;
    const handleClick = () => { if (props.setProps) props.setProps({ n_clicks: n_clicks + 1 }); };
    return (
        <CarbonOverflowMenuItem id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            onClick={handleClick} {...others}>{children}</CarbonOverflowMenuItem>
    );
};

OverflowMenuItem.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func, children: PropTypes.node,
    className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    n_clicks: PropTypes.number, disabled: PropTypes.bool, hasDivider: PropTypes.bool, itemText: PropTypes.string,
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local','session','memory']),
};

OverflowMenuItem.defaultProps = { n_clicks: 0, disabled: false, hasDivider: false };
export default OverflowMenuItem;
