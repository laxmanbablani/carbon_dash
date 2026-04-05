import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * SelectItem is a wrapper for the Carbon SelectItem component.
 */
export default class SelectItem extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { value } = this.props;
        const { text } = this.props;

        const RealComponent = LazyLoader['SelectItem'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    value={value}
                    text={text}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

SelectItem.defaultProps = {
    className: '',
    value: '',
    text: '',
};

SelectItem.propTypes = {
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

    /** n_blur */
    n_blur: PropTypes.number,

    /** n_submit */
    n_submit: PropTypes.number,

    /** debounce */
    debounce: PropTypes.oneOfType([PropTypes.bool, PropTypes.number]),

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * hidden
     */
    hidden: PropTypes.any,

    /**
     * text
     */
    text: PropTypes.string,

    /**
     * value
     */
    value: PropTypes.any,

};
