import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Button is a wrapper for the Carbon Button component.
 */
export default class Button extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { n_clicks } = this.props;

        const RealComponent = LazyLoader['Button'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    n_clicks={n_clicks}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

Button.defaultProps = {
    className: '',
    n_clicks: 0,
};

Button.propTypes = {
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
     * as
     */
    as_: PropTypes.any,

    /**
     * autoAlign
     */
    autoAlign: PropTypes.any,

    /**
     * dangerDescription
     */
    dangerDescription: PropTypes.any,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * hasIconOnly
     */
    hasIconOnly: PropTypes.any,

    /**
     * href
     */
    href: PropTypes.any,

    /**
     * iconDescription
     */
    iconDescription: PropTypes.any,

    /**
     * isExpressive
     */
    isExpressive: PropTypes.any,

    /**
     * isSelected
     */
    isSelected: PropTypes.any,

    /**
     * kind
     */
    kind: PropTypes.any,

    /**
     * onBlur
     */
    onBlur: PropTypes.any,

    /**
     * onClick
     */
    onClick: PropTypes.any,

    /**
     * onFocus
     */
    onFocus: PropTypes.any,

    /**
     * onMouseEnter
     */
    onMouseEnter: PropTypes.any,

    /**
     * onMouseLeave
     */
    onMouseLeave: PropTypes.any,

    /**
     * rel
     */
    rel: PropTypes.any,

    /**
     * renderIcon
     */
    renderIcon: PropTypes.any,

    /**
     * role
     */
    role: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

    /**
     * tabIndex
     */
    tabIndex: PropTypes.any,

    /**
     * target
     */
    target: PropTypes.any,

    /**
     * tooltipAlignment
     */
    tooltipAlignment: PropTypes.any,

    /**
     * tooltipDropShadow
     */
    tooltipDropShadow: PropTypes.any,

    /**
     * tooltipHighContrast
     */
    tooltipHighContrast: PropTypes.any,

    /**
     * tooltipPosition
     */
    tooltipPosition: PropTypes.any,

    /**
     * type
     */
    type: PropTypes.any,

    /**
     * n_clicks
     */
    n_clicks: PropTypes.number,

};
