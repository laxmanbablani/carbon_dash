import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * TableContainer is a wrapper for the Carbon TableContainer component.
 */
export default class TableContainer extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['TableContainer'];
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

TableContainer.defaultProps = {
    className: '',
};

TableContainer.propTypes = {
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
     * aiEnabled
     */
    aiEnabled: PropTypes.any,

    /**
     * decorator
     */
    decorator: PropTypes.any,

    /**
     * description
     */
    description: PropTypes.any,

    /**
     * stickyHeader
     */
    stickyHeader: PropTypes.any,

    /**
     * title
     */
    title: PropTypes.any,

    /**
     * useStaticWidth
     */
    useStaticWidth: PropTypes.any,

};
