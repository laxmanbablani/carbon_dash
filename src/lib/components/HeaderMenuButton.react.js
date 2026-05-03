import React from 'react';
import PropTypes from 'prop-types';
import { HeaderMenuButton as CarbonHeaderMenuButton } from '@carbon/react';
const HeaderMenuButton = (props) => {
    const { id, children, className, style, loading_state, ...others } = props;
    return <CarbonHeaderMenuButton id={id} className={className} style={style} data-dash-is-loading={loading_state?.is_loading||undefined} {...others}/>;
};
HeaderMenuButton.propTypes = {
    id: PropTypes.string, children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    /** Label used for layer navigation with HeaderContainer */
    menuIconDescription: PropTypes.string,
    /** Whether the menu button is active */
    isActive: PropTypes.bool,
};
export default HeaderMenuButton;
