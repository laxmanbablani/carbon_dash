import React from 'react';
import PropTypes from 'prop-types';
import { MenuItem as CarbonMenuItem } from '@carbon/react';

/**
 * MenuItem is a component for rendering menu items within ComboButton or OverflowMenu.
 * 
 * Usage with ComboButton:
 * <ComboButton label="Primary action">
 *   <MenuItem label="Second action" />
 *   <MenuItem label="Third action" />
 * </ComboButton>
 */
const MenuItem = (props) => {
    const {
        id,
        label,
        kind,
        disabled = false,
        ...others
    } = props;

    return (
        <CarbonMenuItem
            id={id}
            label={label}
            kind={kind}
            disabled={disabled}
            {...others}
        />
    );
};

MenuItem.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

    /** Dash callback to update props */
    setProps: PropTypes.func,

    /** Specify the label of the menu item */
    label: PropTypes.string.isRequired,

    /** Specify the kind of menu item */
    kind: PropTypes.oneOf(['danger']),

    /** Specify whether the menu item is disabled */
    disabled: PropTypes.bool,
};

MenuItem.propTypes.description = 'MenuItem is a component for rendering menu items within ComboButton or OverflowMenu.';

MenuItem.defaultProps = {
    disabled: false,
};

export default MenuItem;