import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * FileUploader is a wrapper for the Carbon FileUploader component.
 */
export default class FileUploader extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['FileUploader'];
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

FileUploader.defaultProps = {
    className: '',
};

FileUploader.propTypes = {
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
     * accept
     */
    accept: PropTypes.any,

    /**
     * buttonKind
     */
    buttonKind: PropTypes.any,

    /**
     * buttonLabel
     */
    buttonLabel: PropTypes.any,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * filenameStatus
     */
    filenameStatus: PropTypes.any,

    /**
     * iconDescription
     */
    iconDescription: PropTypes.any,

    /**
     * labelDescription
     */
    labelDescription: PropTypes.any,

    /**
     * labelTitle
     */
    labelTitle: PropTypes.any,

    /**
     * maxFileSize
     */
    maxFileSize: PropTypes.any,

    /**
     * multiple
     */
    multiple: PropTypes.any,

    /**
     * name
     */
    name: PropTypes.any,

    /**
     * onAddFiles
     */
    onAddFiles: PropTypes.any,

    /**
     * onChange
     */
    onChange: PropTypes.any,

    /**
     * onClick
     */
    onClick: PropTypes.any,

    /**
     * onDelete
     */
    onDelete: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

};
