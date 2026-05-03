import React from 'react';
import PropTypes from 'prop-types';
import { SideNavLink as CarbonSideNavLink } from '@carbon/react';
import { getLoadingState } from '../utils/dash';
import { resolveIcon } from '../utils/resolveIcon';

const SideNavLink = (props) => {
    const { id, children, className = '', style = {}, loading_state, renderIcon, n_clicks = 0, ...others } = props;
    const iconElement = resolveIcon(renderIcon);
    const handleClick = () => { if (props.setProps) props.setProps({ n_clicks: n_clicks + 1 }); };
    return (
        <CarbonSideNavLink id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            renderIcon={iconElement} onClick={handleClick} {...others}>{children}</CarbonSideNavLink>
    );
};

SideNavLink.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func, children: PropTypes.node,
    className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    renderIcon: PropTypes.node, n_clicks: PropTypes.number, href: PropTypes.string, isActive: PropTypes.bool,
    isSideNavExpanded: PropTypes.bool, large: PropTypes.bool, tabIndex: PropTypes.number,
    ariaLabel: PropTypes.string, ariaLabelledBy: PropTypes.string,
    as: PropTypes.elementType, element: PropTypes.elementType,
};
SideNavLink.defaultProps = { n_clicks: 0, large: false };

export default SideNavLink;
