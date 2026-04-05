import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Accordion is a wrapper for the Carbon Accordion component.
 */
export default class Accordion extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { align } = this.props;
        const { isFlush } = this.props;
        const { size } = this.props;

        const RealComponent = LazyLoader['Accordion'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    align={align}
                    isFlush={isFlush}
                    size={size}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

Accordion.defaultProps = {
    className: '',
    align: 'end',
    isFlush: false,
    size: 'md',
};

Accordion.propTypes = {
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
    align: PropTypes.string,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * isFlush
     */
    isFlush: PropTypes.bool,

    /**
     * ordered
     */
    ordered: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.string,

};
