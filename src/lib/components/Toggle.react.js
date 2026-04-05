import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Toggle is a wrapper for the Carbon Toggle component.
 */
export default class Toggle extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { toggled } = this.props;
        const { label } = this.props;

        const RealComponent = LazyLoader['Toggle'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    toggled={toggled}
                    label={label}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

Toggle.defaultProps = {
    className: '',
    toggled: false,
    label: 'Toggle',
};

Toggle.propTypes = {
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
     * defaultToggled
     */
    defaultToggled: PropTypes.any,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * hideLabel
     */
    hideLabel: PropTypes.any,

    /**
     * labelA
     */
    labelA: PropTypes.any,

    /**
     * labelB
     */
    labelB: PropTypes.any,

    /**
     * labelText
     */
    labelText: PropTypes.any,

    /**
     * onClick
     */
    onClick: PropTypes.any,

    /**
     * onToggle
     */
    onToggle: PropTypes.any,

    /**
     * readOnly
     */
    readOnly: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

    /**
     * toggled
     */
    toggled: PropTypes.bool,

    /**
     * label
     */
    label: PropTypes.string,

};
