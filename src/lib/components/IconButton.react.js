import React from 'react';
import PropTypes from 'prop-types';
import { IconButton as CarbonIconButton } from '@carbon/react';
import { getLoadingState } from '../utils/dash';
import { resolveIcon } from '../utils/resolveIcon';

const IconButton = (props) => {
    const { id, children, className = '', style = {}, loading_state, renderIcon, n_clicks = 0, ...others } = props;
    const handleClick = () => { if (props.setProps) props.setProps({ n_clicks: n_clicks + 1 }); };
    const icon = resolveIcon(renderIcon);
    return <CarbonIconButton id={id} className={className} style={style} renderIcon={icon} onClick={handleClick} data-dash-is-loading={getLoadingState(loading_state) || undefined} {...others}>{children}</CarbonIconButton>;
};
IconButton.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func, children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    renderIcon: PropTypes.node, n_clicks: PropTypes.number, disabled: PropTypes.bool, kind: PropTypes.oneOf(['primary','secondary','tertiary','ghost','danger']),
    size: PropTypes.oneOf(['sm','md','lg']), label: PropTypes.string, hasIconOnly: PropTypes.bool, tooltipAlignment: PropTypes.string, tooltipPosition: PropTypes.string,
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string), persistence_type: PropTypes.oneOf(['local','session','memory']),
};
IconButton.defaultProps = { n_clicks: 0, disabled: false, kind: 'primary', size: 'lg' };
export default IconButton;
