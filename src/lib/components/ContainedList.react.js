import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * ContainedList is a wrapper for the Carbon ContainedList component.
 */
export default class ContainedList extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['ContainedList'];
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

ContainedList.defaultProps = {
    className: '',
};

ContainedList.propTypes = {
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
     * action
     */
    action: PropTypes.any,

    /**
     * isInset
     */
    isInset: PropTypes.any,

    /**
     * kind
     */
    kind: PropTypes.any,

    /**
     * label
     */
    label: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

};
