import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * MenuItem is a wrapper for the Carbon MenuItem component.
 */
export default class MenuItem extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['MenuItem'];
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

MenuItem.defaultProps = {
    className: '',
};

MenuItem.propTypes = {
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
     * dangerDescription
     */
    dangerDescription: PropTypes.any,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * kind
     */
    kind: PropTypes.any,

    /**
     * label
     */
    label: PropTypes.any,

    /**
     * onClick
     */
    onClick: PropTypes.any,

    /**
     * renderIcon
     */
    renderIcon: PropTypes.any,

    /**
     * shortcut
     */
    shortcut: PropTypes.any,

};
