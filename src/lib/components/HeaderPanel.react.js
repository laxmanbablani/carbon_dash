import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * HeaderPanel is a wrapper for the Carbon HeaderPanel component.
 */
export default class HeaderPanel extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { expanded } = this.props;

        const RealComponent = LazyLoader['HeaderPanel'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    expanded={expanded}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

HeaderPanel.defaultProps = {
    className: '',
    expanded: false,
};

HeaderPanel.propTypes = {
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
     * addFocusListeners
     */
    addFocusListeners: PropTypes.any,

    /**
     * expanded
     */
    expanded: PropTypes.bool,

    /**
     * href
     */
    href: PropTypes.any,

    /**
     * onHeaderPanelFocus
     */
    onHeaderPanelFocus: PropTypes.any,

};
