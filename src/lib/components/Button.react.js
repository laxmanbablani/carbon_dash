import React from 'react';
import PropTypes from 'prop-types';
import { Button as CarbonButton, ButtonSkeleton as CarbonButtonSkeleton, AILabel } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

/**
 * Button is a wrapper for the Carbon Button component.
 */
const Button = (props) => {
    const {
        id,
        setProps,
        children,
        className = '',
        style = {},
        loading_state,
        n_clicks = 0,
        kind = 'primary',
        size = 'lg',
        disabled = false,
        isExpressive = false,
        isSelected = false,
        hasIconOnly = false,
        dangerDescription,
        iconDescription,
        href,
        renderIcon,
        tooltipAlignment,
        tooltipPosition,
        aiLabel = false,
        ...others
    } = props;

    // Show skeleton while loading
    if (loading_state && loading_state.is_loading) {
        return (
            <CarbonButtonSkeleton
                id={id}
                className={className}
                style={style}
                size={size}
            />
        );
    }

    const handleClick = () => {
        if (setProps) {
            setProps({ n_clicks: n_clicks + 1, n_clicks_timestamp: Date.now() });
        }
    };

    const iconElement = resolveIcon(renderIcon);
    const decorator = aiLabel ? React.createElement(AILabel, { size: 'xs' }) : undefined;

    return (
        <CarbonButton
            id={id}
            className={className}
            style={style}
            kind={kind}
            size={size}
            disabled={disabled}
            isExpressive={isExpressive}
            isSelected={isSelected}
            hasIconOnly={hasIconOnly}
            dangerDescription={dangerDescription}
            iconDescription={iconDescription}
            href={href}
            renderIcon={iconElement}
            tooltipAlignment={tooltipAlignment}
            tooltipPosition={tooltipPosition}
            decorator={decorator}
            onClick={handleClick}
            {...others}
        >
            {children}
        </CarbonButton>
    );
};

Button.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Dash-assigned callback for reactivity.
     */
    setProps: PropTypes.func,

    /**
     * The content of the button.
     */
    children: PropTypes.node,

    /**
     * Specify a custom className to be applied to the component.
     */
    className: PropTypes.string,

    /**
     * Inline styles.
     */
    style: PropTypes.object,

    /**
     * Dash loading state.
     */
    loading_state: PropTypes.shape({
        is_loading: PropTypes.bool,
        prop_name: PropTypes.string,
        component_name: PropTypes.string,
    }),

    /**
     * An integer that represents the number of times that this element has been clicked.
     */
    n_clicks: PropTypes.number,

    /**
     * Timestamp of the last click in milliseconds since epoch.
     */
    n_clicks_timestamp: PropTypes.number,

    /**
     * Specify the kind of button. Default: 'primary'.
     */
    kind: PropTypes.oneOf(['primary', 'secondary', 'tertiary', 'ghost', 'danger']),

    /**
     * Specify the size of the button. Default: 'lg'.
     */
    size: PropTypes.oneOf(['sm', 'md', 'lg', 'xl', '2xl']),

    /**
     * Whether the button is disabled.
     */
    disabled: PropTypes.bool,

    /**
     * Enable expressive styling.
     */
    isExpressive: PropTypes.bool,

    /**
     * Whether the button is in a selected state.
     */
    isSelected: PropTypes.bool,

    /**
     * Whether the button should only render an icon.
     */
    hasIconOnly: PropTypes.bool,

    /**
     * Description for the danger variant (screen readers).
     */
    dangerDescription: PropTypes.string,

    /**
     * Icon description for screen readers.
     */
    iconDescription: PropTypes.string,

    /**
     * If provided, renders as a link.
     */
    href: PropTypes.string,

    /**
     * An icon component to render in the button.
     * Accepts DashIconify, html.Div, Carbon icon name string, or any React node.
     */
    renderIcon: PropTypes.node,

    /**
     * Tooltip alignment.
     */
    tooltipAlignment: PropTypes.oneOf(['start', 'center', 'end']),

    /**
     * Tooltip position.
     */
    tooltipPosition: PropTypes.oneOf(['top', 'bottom', 'left', 'right']),

    /**
     * Whether to render the AI label decorator.
     */
    aiLabel: PropTypes.bool,

    /**
     * Used to allow user interactions in this component to be persisted.
     */
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),

    /**
     * Properties whose user interactions will persist.
     */
    persisted_props: PropTypes.arrayOf(PropTypes.string),

    /**
     * Where persisted user changes will be stored.
     */
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

Button.defaultProps = {
    kind: 'primary',
    size: 'lg',
    disabled: false,
    isExpressive: false,
    isSelected: false,
    hasIconOnly: false,
    aiLabel: false,
    n_clicks: 0,
};

export default Button;
