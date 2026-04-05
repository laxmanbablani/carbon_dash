import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * DismissibleTag is a wrapper for the Carbon DismissibleTag component.
 */
export default class DismissibleTag extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['DismissibleTag'];
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

DismissibleTag.defaultProps = {
    className: '',
};

DismissibleTag.propTypes = {
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
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * dismissTooltipAlignment
     */
    dismissTooltipAlignment: PropTypes.any,

    /**
     * dismissTooltipLabel
     */
    dismissTooltipLabel: PropTypes.any,

    /**
     * onClose
     */
    onClose: PropTypes.any,

    /**
     * renderIcon
     */
    renderIcon: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

    /**
     * slug
     */
    slug: PropTypes.any,

    /**
     * text
     */
    text: PropTypes.any,

    /**
     * tagTitle
     */
    tagTitle: PropTypes.any,

    /**
     * title
     */
    title: PropTypes.any,

    /**
     * type
     */
    type: PropTypes.any,

};
