import React from 'react';
import PropTypes from 'prop-types';
import { MenuItemDivider as CarbonMenuItemDivider } from '@carbon/react';

/**
 * MenuItemDivider is a divider component for use within ComboButton or OverflowMenu.
 * 
 * Usage:
 * <ComboButton label="Primary action">
 *   <MenuItem label="Second action" />
 *   <MenuItemDivider />
 *   <MenuItem label="Third action" />
 * </ComboButton>
 */
const MenuItemDivider = (props) => {
    return <CarbonMenuItemDivider {...props} />;
};

MenuItemDivider.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,
    
    /** Dash callback to update props */
    setProps: PropTypes.func,
};

MenuItemDivider.propTypes.description = 'MenuItemDivider is a divider component for use within ComboButton or OverflowMenu.';

export default MenuItemDivider;