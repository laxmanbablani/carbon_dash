import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * ProgressIndicator is a wrapper for the Carbon ProgressIndicator component.
 */
export default class ProgressIndicator extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { currentIndex } = this.props;
        const { vertical } = this.props;
        const { spaceEqually } = this.props;

        const RealComponent = LazyLoader['ProgressIndicator'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    currentIndex={currentIndex}
                    vertical={vertical}
                    spaceEqually={spaceEqually}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

ProgressIndicator.defaultProps = {
    className: '',
    currentIndex: 0,
    vertical: false,
    spaceEqually: false,
};

ProgressIndicator.propTypes = {
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
     * currentIndex
     */
    currentIndex: PropTypes.number,

    /**
     * onChange
     */
    onChange: PropTypes.any,

    /**
     * spaceEqually
     */
    spaceEqually: PropTypes.bool,

    /**
     * vertical
     */
    vertical: PropTypes.bool,

};
