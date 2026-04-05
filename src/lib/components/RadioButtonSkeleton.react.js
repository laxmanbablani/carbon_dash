import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * RadioButtonSkeleton is a wrapper for the Carbon RadioButtonSkeleton component.
 */
export default class RadioButtonSkeleton extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['RadioButtonSkeleton'];
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

RadioButtonSkeleton.defaultProps = {
    className: '',
};

RadioButtonSkeleton.propTypes = {
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

};
