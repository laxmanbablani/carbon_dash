import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * FileUploaderDropContainer is a wrapper for the Carbon FileUploaderDropContainer component.
 */
export default class FileUploaderDropContainer extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['FileUploaderDropContainer'];
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

FileUploaderDropContainer.defaultProps = {
    className: '',
};

FileUploaderDropContainer.propTypes = {
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
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * labelText
     */
    labelText: PropTypes.any,

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
     * onClick
     */
    onClick: PropTypes.any,

    /**
     * pattern
     */
    pattern: PropTypes.any,

    /**
     * role
     */
    role: PropTypes.any,

    /**
     * tabIndex
     */
    tabIndex: PropTypes.any,

};
