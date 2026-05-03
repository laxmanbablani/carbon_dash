import React from 'react';
import PropTypes from 'prop-types';
import { ComboButton as CarbonComboButton } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * ComboButton is a button with a menu attached for additional actions.
 * It renders a primary button with a dropdown menu of secondary actions.
 * 
 * Children should be Carbon MenuItem components (e.g., cd.MenuItem(label="Action")).
 * These can be created using carbon_dash.MenuItem in Python.
 */
const ComboButton = (props) => {
    const {
        id,
        children,
        className = '',
        style = {},
        loading_state,
        label,
        menuAlignment = 'bottom',
        tooltipAlignment,
        size,
        kind = 'primary',
        disabled = false,
        ...others
    } = props;

    const handleClick = () => {
        if (props.setProps) {
            props.setProps({ n_clicks: (props.n_clicks || 0) + 1 });
        }
    };

    if (loading_state && loading_state.is_loading) {
        return <CarbonComboButton label={label} className={className} disabled />;
    }

    return (
        <CarbonComboButton
            id={id}
            className={className}
            style={style}
            label={label}
            menuAlignment={menuAlignment}
            tooltipAlignment={tooltipAlignment}
            size={size}
            kind={kind}
            disabled={disabled}
            onClick={handleClick}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonComboButton>
    );
};

ComboButton.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

    /** Dash callback to update props */
    setProps: PropTypes.func,

    /** The content of the ComboButton (MenuItem components) */
    children: PropTypes.node,

    /** Custom CSS class */
    className: PropTypes.string,

    /** Inline styles */
    style: PropTypes.object,

    /** Dash loading state */
    loading_state: PropTypes.shape({
        is_loading: PropTypes.bool,
        prop_name: PropTypes.string,
        component_name: PropTypes.string,
    }),

    /** The label text for the primary button */
    label: PropTypes.string.isRequired,

    /** Specify the alignment of the menu relative to the button */
    menuAlignment: PropTypes.oneOf(['top', 'top-start', 'top-end', 'bottom', 'bottom-start', 'bottom-end']),

    /** Specify the alignment of the tooltip */
    tooltipAlignment: PropTypes.oneOf(['start', 'center', 'end']),

    /** Specify the size of the button */
    size: PropTypes.oneOf(['sm', 'md', 'lg', 'xl']),

    /** Specify the kind of button */
    kind: PropTypes.oneOf(['primary', 'secondary', 'tertiary', 'ghost', 'danger']),

    /** Specify whether the ComboButton should be disabled */
    disabled: PropTypes.bool,

    /** Number of times the button has been clicked */
    n_clicks: PropTypes.number,
};

ComboButton.defaultProps = {
    menuAlignment: 'bottom',
    kind: 'primary',
    disabled: false,
    n_clicks: 0,
};

export default ComboButton;