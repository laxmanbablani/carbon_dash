import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * RadioButtonGroup is a wrapper for the Carbon RadioButtonGroup component.
 */
export default class RadioButtonGroup extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { valueSelected } = this.props;
        const { label } = this.props;

        const RealComponent = LazyLoader['RadioButtonGroup'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    valueSelected={valueSelected}
                    label={label}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

RadioButtonGroup.defaultProps = {
    className: '',
    valueSelected: null,
    label: 'Radio Button Group',
};

RadioButtonGroup.propTypes = {
    /** id */
    id: PropTypes.string,

    /** children */
    children: PropTypes.node,

    /** className */
    className: PropTypes.string,

    /** style */
    style: PropTypes.object,

    /** setProps */
    setProps: PropTypes.func,

    /** loading_state */
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),

    /** persistence */
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),

    /** persisted_props */
    persisted_props: PropTypes.arrayOf(PropTypes.string),

    /** persistence_type */
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),

    /**
     * decorator
     */
    decorator: PropTypes.any,

    /**
     * defaultSelected
     */
    defaultSelected: PropTypes.any,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * helperText
     */
    helperText: PropTypes.any,

    /**
     * invalid
     */
    invalid: PropTypes.any,

    /**
     * invalidText
     */
    invalidText: PropTypes.any,

    /**
     * labelPosition
     */
    labelPosition: PropTypes.any,

    /**
     * legendText
     */
    legendText: PropTypes.any,

    /**
     * name
     */
    name: PropTypes.any,

    /**
     * onChange
     */
    onChange: PropTypes.any,

    /**
     * orientation
     */
    orientation: PropTypes.any,

    /**
     * readOnly
     */
    readOnly: PropTypes.any,

    /**
     * required
     */
    required: PropTypes.any,

    /**
     * slug
     */
    slug: PropTypes.any,

    /**
     * valueSelected
     */
    valueSelected: PropTypes.any,

    /**
     * warn
     */
    warn: PropTypes.any,

    /**
     * warnText
     */
    warnText: PropTypes.any,

    /**
     * label
     */
    label: PropTypes.string,

};
