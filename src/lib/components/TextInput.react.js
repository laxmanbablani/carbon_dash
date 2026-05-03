import React from 'react';
import PropTypes from 'prop-types';
import { TextInput as CarbonTextInput, TextInputSkeleton as CarbonTextInputSkeleton, AILabel } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * TextInput is a wrapper for the Carbon TextInput component.
 * Supports label, placeholder, helper text, invalid/warn states, and AI label decorator.
 */
const TextInput = (props) => {
    const {
        id, children, className = '', style = {}, loading_state,
        value, aiLabel = false, renderIcon,
        ...others
    } = props;

    if (loading_state && loading_state.is_loading) {
        return <CarbonTextInputSkeleton id={id} className={className} hideLabel={false} />;
    }

    const handleChange = (e) => {
        if (props.setProps) props.setProps({ value: e.target?.value ?? e });
    };

    const decorator = aiLabel ? React.createElement(AILabel, { size: 'xs' }) : undefined;

    return (
        <CarbonTextInput
            id={id}
            className={className}
            style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            value={value}
            onChange={handleChange}
            decorator={decorator}
            renderIcon={renderIcon}
            {...others}
        >
            {children}
        </CarbonTextInput>
    );
};

TextInput.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,
    /** Dash-assigned callback for reactivity */
    setProps: PropTypes.func,
    /** The content of the text input (used as label fallback if labelText not provided) */
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
    /** The value of the input */
    value: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
    /** Specify the label text */
    labelText: PropTypes.node,
    /** Placeholder text */
    placeholder: PropTypes.string,
    /** Input helper text */
    helperText: PropTypes.node,
    /** Whether the input is disabled */
    disabled: PropTypes.bool,
    /** Whether the input is read only */
    readOnly: PropTypes.bool,
    /** Whether the input is in an invalid state */
    invalid: PropTypes.bool,
    /** Invalid state error message */
    invalidText: PropTypes.node,
    /** Whether the input is in a warning state */
    warn: PropTypes.bool,
    /** Warning state message */
    warnText: PropTypes.node,
    /** Size of the input */
    size: PropTypes.oneOf(['sm', 'md', 'lg']),
    /** Whether to hide the label */
    hideLabel: PropTypes.bool,
    /** Whether to display the character counter */
    enableCounter: PropTypes.bool,
    /** Maximum count (used with enableCounter) */
    maxCount: PropTypes.number,
    /** What the input type is (e.g. 'text', 'email', 'password') */
    type: PropTypes.string,
    /** Default value (for uncontrolled mode) */
    defaultValue: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
    /** Whether the label should be lightweight */
    light: PropTypes.bool,
    /** An icon component to render inside the input */
    renderIcon: PropTypes.node,
    /** Whether to render the AI label decorator */
    aiLabel: PropTypes.bool,
    /** Callback for when the input value changes */
    onChange: PropTypes.func,
    /** Callback for when the input loses focus */
    onBlur: PropTypes.func,
    /** Persistence */
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

TextInput.defaultProps = {
    disabled: false,
    invalid: false,
    warn: false,
    hideLabel: false,
    readOnly: false,
    size: 'md',
    aiLabel: false,
};

export default TextInput;
