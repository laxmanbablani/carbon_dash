import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * AccordionSkeleton is a wrapper for the Carbon AccordionSkeleton component.
 */
export default class AccordionSkeleton extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['AccordionSkeleton'];
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

AccordionSkeleton.defaultProps = {
    className: '',
};

AccordionSkeleton.propTypes = {
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
     * count
     */
    count: PropTypes.any,

    /**
     * isFlush
     */
    isFlush: PropTypes.any,

    /**
     * open
     */
    open: PropTypes.any,

    /**
     * ordered
     */
    ordered: PropTypes.any,

};
