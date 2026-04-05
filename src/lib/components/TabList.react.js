import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * TabList is a wrapper for the Carbon TabList component.
 */
export default class TabList extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { contained } = this.props;

        const RealComponent = LazyLoader['TabList'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    contained={contained}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

TabList.defaultProps = {
    className: '',
    contained: false,
};

TabList.propTypes = {
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
     * activation
     */
    activation: PropTypes.any,

    /**
     * contained
     */
    contained: PropTypes.bool,

    /**
     * fullWidth
     */
    fullWidth: PropTypes.any,

    /**
     * iconSize
     */
    iconSize: PropTypes.any,

    /**
     * leftOverflowButtonProps
     */
    leftOverflowButtonProps: PropTypes.any,

    /**
     * light
     */
    light: PropTypes.any,

    /**
     * rightOverflowButtonProps
     */
    rightOverflowButtonProps: PropTypes.any,

    /**
     * scrollDebounceWait
     */
    scrollDebounceWait: PropTypes.any,

    /**
     * scrollIntoView
     */
    scrollIntoView: PropTypes.any,

};
