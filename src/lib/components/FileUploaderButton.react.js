import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * FileUploaderButton is a wrapper for the Carbon FileUploaderButton component.
 */
export default class FileUploaderButton extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['FileUploaderButton'];
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

FileUploaderButton.defaultProps = {
    className: '',
};

FileUploaderButton.propTypes = {
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
     * disableLabelChanges
     */
    disableLabelChanges: PropTypes.any,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * labelText
     */
    labelText: PropTypes.any,

    /**
     * multiple
     */
    multiple: PropTypes.any,

    /**
     * name
     */
    name: PropTypes.any,

    /**
     * onChange
     */
    onChange: PropTypes.any,

    /**
     * onClick
     */
    onClick: PropTypes.any,

    /**
     * role
     */
    role: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

    /**
     * tabIndex
     */
    tabIndex: PropTypes.any,

};
