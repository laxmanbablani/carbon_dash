import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * FileUploaderItem is a wrapper for the Carbon FileUploaderItem component.
 */
export default class FileUploaderItem extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['FileUploaderItem'];
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

FileUploaderItem.defaultProps = {
    className: '',
};

FileUploaderItem.propTypes = {
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
     * errorBody
     */
    errorBody: PropTypes.any,

    /**
     * errorSubject
     */
    errorSubject: PropTypes.any,

    /**
     * iconDescription
     */
    iconDescription: PropTypes.any,

    /**
     * invalid
     */
    invalid: PropTypes.any,

    /**
     * name
     */
    name: PropTypes.any,

    /**
     * onDelete
     */
    onDelete: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

    /**
     * status
     */
    status: PropTypes.any,

    /**
     * uuid
     */
    uuid: PropTypes.any,

};
