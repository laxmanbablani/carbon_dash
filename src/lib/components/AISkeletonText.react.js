import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * AISkeletonText is a wrapper for the Carbon AISkeletonText component.
 */
export default class AISkeletonText extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['AISkeletonText'];
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

AISkeletonText.defaultProps = {
    className: '',
};

AISkeletonText.propTypes = {
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
     * heading
     */
    heading: PropTypes.any,

    /**
     * lineCount
     */
    lineCount: PropTypes.any,

    /**
     * paragraph
     */
    paragraph: PropTypes.any,

    /**
     * width
     */
    width: PropTypes.any,

};
