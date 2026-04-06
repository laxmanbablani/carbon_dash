import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * ExpandableTile is a wrapper for the Carbon ExpandableTile component.
 */
export default class ExpandableTile extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { expanded } = this.props;

        const RealComponent = LazyLoader['ExpandableTile'];
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

ExpandableTile.defaultProps = {
    className: '',
    expanded: false,
};

ExpandableTile.propTypes = {
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
     * decorator
     */
    decorator: PropTypes.any,

    /**
     * expanded
     */
    expanded: PropTypes.bool,

    /**
     * hasRoundedCorners
     */
    hasRoundedCorners: PropTypes.any,

    /**
     * light
     */
    light: PropTypes.any,

    /**
     * onClick
     */
    onClick: PropTypes.any,

    /**
     * onKeyUp
     */
    onKeyUp: PropTypes.any,

    /**
     * slug
     */
    slug: PropTypes.any,

    /**
     * tabIndex
     */
    tabIndex: PropTypes.any,

    /**
     * tileCollapsedIconText
     */
    tileCollapsedIconText: PropTypes.node,

    /**
     * tileCollapsedLabel
     */
    tileCollapsedLabel: PropTypes.any,

    /**
     * tileExpandedIconText
     */
    tileExpandedIconText: PropTypes.node,

    /**
     * tileExpandedLabel
     */
    tileExpandedLabel: PropTypes.any,

};
