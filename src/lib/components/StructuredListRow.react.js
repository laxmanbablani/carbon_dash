import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * StructuredListRow is a wrapper for the Carbon StructuredListRow component.
 */
export default class StructuredListRow extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['StructuredListRow'];
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

StructuredListRow.defaultProps = {
    className: '',
};

StructuredListRow.propTypes = {
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
     * head
     */
    head: PropTypes.any,

    /**
     * label
     */
    label: PropTypes.any,

    /**
     * onClick
     */
    onClick: PropTypes.any,

    /**
     * onKeyDown
     */
    onKeyDown: PropTypes.any,

    /**
     * selection
     */
    selection: PropTypes.any,

};
