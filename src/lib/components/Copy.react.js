import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Copy is a wrapper for the Carbon Copy component.
 */
export default class Copy extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['Copy'];
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

Copy.defaultProps = {
    className: '',
};

Copy.propTypes = {
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
     * autoAlign
     */
    autoAlign: PropTypes.any,

    /**
     * feedback
     */
    feedback: PropTypes.any,

    /**
     * feedbackTimeout
     */
    feedbackTimeout: PropTypes.any,

    /**
     * onAnimationEnd
     */
    onAnimationEnd: PropTypes.any,

    /**
     * onClick
     */
    onClick: PropTypes.any,

};
