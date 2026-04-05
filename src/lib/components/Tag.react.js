import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Tag is a wrapper for the Carbon Tag component.
 */
export default class Tag extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { type } = this.props;
        const { size } = this.props;
        const { disabled } = this.props;

        const RealComponent = LazyLoader['Tag'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    type={type}
                    size={size}
                    disabled={disabled}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

Tag.defaultProps = {
    className: '',
    type: 'gray',
    size: 'md',
    disabled: false,
};

Tag.propTypes = {
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
     * as
     */
    as_: PropTypes.any,

    /**
     * decorator
     */
    decorator: PropTypes.any,

    /**
     * disabled
     */
    disabled: PropTypes.bool,

    /**
     * filter
     */
    filter: PropTypes.any,

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
    size: PropTypes.string,

    /**
     * slug
     */
    slug: PropTypes.any,

    /**
     * title
     */
    title: PropTypes.any,

    /**
     * type
     */
    type: PropTypes.string,

};
