import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * IconSwitch is a wrapper for the Carbon IconSwitch component.
 */
export default class IconSwitch extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['IconSwitch'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

IconSwitch.defaultProps = {
    className: '',
};

IconSwitch.propTypes = {
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

    /**
     * align
     */
    align: PropTypes.any,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * enterDelayMs
     */
    enterDelayMs: PropTypes.any,

    /**
     * index
     */
    index: PropTypes.any,

    /**
     * leaveDelayMs
     */
    leaveDelayMs: PropTypes.any,

    /**
     * name
     */
    name: PropTypes.any,

    /**
     * onClick
     */
    onClick: PropTypes.any,

    /**
     * onKeyDown
     */
    onKeyDown: PropTypes.any,

    /**
     * selected
     */
    selected: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

    /**
     * text
     */
    text: PropTypes.any,

};
