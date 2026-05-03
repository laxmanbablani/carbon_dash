import React from 'react';
import PropTypes from 'prop-types';
import { Slider as CarbonSlider, SliderSkeleton as CarbonSliderSkeleton } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const Slider = (props) => {
    const { id, children, className = '', style = {}, loading_state, value, ...others } = props;

    if (loading_state && loading_state.is_loading) {
        return <CarbonSliderSkeleton id={id} className={className} />;
    }

    const handleChange = (e) => {
        if (props.setProps) props.setProps({ value: e?.value ?? e?.target?.value ?? e });
    };

    return (
        <CarbonSlider
            id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            value={value}
            onChange={handleChange}
            {...others}
        />
    );
};

Slider.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func,
    children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    /** Current value */
    value: PropTypes.number,
    /** Label text */
    labelText: PropTypes.node,
    /** Minimum value */
    min: PropTypes.number,
    /** Maximum value */
    max: PropTypes.number,
    /** Step interval */
    step: PropTypes.number,
    /** Step multipliers array */
    stepMultiplier: PropTypes.number,
    /** Whether disabled */
    disabled: PropTypes.bool,
    /** Whether to hide text inputs */
    hideTextInput: PropTypes.bool,
    /** Minimum label */
    minLabel: PropTypes.string,
    /** Maximum label */
    maxLabel: PropTypes.string,
    /** Label for current value */
    valueLabel: PropTypes.string,
    /** Format for value label */
    formatLabel: PropTypes.func,
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

Slider.defaultProps = { disabled: false, hideTextInput: false, min: 0, max: 100, step: 1 };

export default Slider;
