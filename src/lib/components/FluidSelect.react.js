import React from 'react';
import PropTypes from 'prop-types';
import { FluidSelect as CarbonFluidSelect, FluidSelectSkeleton as CarbonFluidSelectSkeleton, SelectItem as CarbonSelectItem } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * FluidSelect is a full-width Select component.
 */
const FluidSelect = (props) => {
    const {
        id,
        children,
        className = '',
        style = {},
        loading_state,
        labelText,
        helperText,
        invalid,
        invalidText,
        warn,
        warnText,
        disabled = false,
        ...others
    } = props;

    if (loading_state && loading_state.is_loading) {
        return <CarbonFluidSelectSkeleton id={id} className={className} />;
    }

    const handleChange = ({ selectedItem }) => {
        if (props.setProps) {
            props.setProps({ selectedItem });
        }
    };

    return (
        <CarbonFluidSelect
            id={id}
            className={className}
            style={style}
            labelText={labelText}
            helperText={helperText}
            invalid={invalid}
            invalidText={invalidText}
            warn={warn}
            warnText={warnText}
            disabled={disabled}
            onChange={handleChange}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonFluidSelect>
    );
};

FluidSelect.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

    /** Dash callback to update props */
    setProps: PropTypes.func,

    /** The content of the select (SelectItem components) */
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

    /** Provide text that is used alongside the control label for additional help */
    labelText: PropTypes.node,

    /** Provide text that is used alongside the control label for additional help */
    helperText: PropTypes.node,

    /** Specify whether the control is currently in an invalid state */
    invalid: PropTypes.bool,

    /** Provide the text that is displayed when the control is in an invalid state */
    invalidText: PropTypes.node,

    /** Specify whether the control is currently in a warning state */
    warn: PropTypes.bool,

    /** Provide the text that is displayed when the control is in a warning state */
    warnText: PropTypes.node,

    /** Specify whether the control is disabled */
    disabled: PropTypes.bool,

    /** Specify the size of the select */
    size: PropTypes.oneOf(['sm', 'md', 'lg']),

    /** Persistence settings */
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

FluidSelect.defaultProps = {
    disabled: false,
    invalid: false,
    warn: false,
    size: 'md',
};

export default FluidSelect;