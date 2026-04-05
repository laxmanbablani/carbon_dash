import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * StructuredListWrapper is a wrapper for the Carbon StructuredListWrapper component.
 */
export default class StructuredListWrapper extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['StructuredListWrapper'];
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

StructuredListWrapper.defaultProps = {
    className: '',
};

StructuredListWrapper.propTypes = {
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
     * ariaLabel
     */
    ariaLabel: PropTypes.any,

    /**
     * isCondensed
     */
    isCondensed: PropTypes.any,

    /**
     * isFlush
     */
    isFlush: PropTypes.any,

    /**
     * selection
     */
    selection: PropTypes.any,

    /**
     * selectedInitialRow
     */
    selectedInitialRow: PropTypes.any,

};
