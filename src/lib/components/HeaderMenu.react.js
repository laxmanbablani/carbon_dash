import React from 'react';
import PropTypes from 'prop-types';
import { HeaderMenu as CarbonHeaderMenu } from '@carbon/react';
const HeaderMenu = (props) => {
    const { id, children, className, style, loading_state, ...others } = props;
    return <CarbonHeaderMenu id={id} className={className} style={style} data-dash-is-loading={loading_state?.is_loading||undefined} {...others}>{children}</CarbonHeaderMenu>;
};
HeaderMenu.propTypes = {
    id: PropTypes.string, children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    /** Menu link name for accessibility */
    ariaLabel: PropTypes.string,
    /** The label for the menu */
    menuLinkName: PropTypes.string,
    /** Whether the menu is active */
    isActive: PropTypes.bool,
};
export default HeaderMenu;
