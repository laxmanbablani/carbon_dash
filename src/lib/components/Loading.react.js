import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Loading is a wrapper for the Carbon Loading component.
 */
export default class Loading extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { active } = this.props;
        const { withOverlay } = this.props;
        const { small } = this.props;

        const RealComponent = LazyLoader['Loading'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    active={active}
                    withOverlay={withOverlay}
                    small={small}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

Loading.defaultProps = {
    className: '',
    active: true,
    withOverlay: true,
    small: false,
};

Loading.propTypes = {
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
     * active
     */
    active: PropTypes.bool,

    /**
     * description
     */
    description: PropTypes.any,

    /**
     * small
     */
    small: PropTypes.bool,

    /**
     * withOverlay
     */
    withOverlay: PropTypes.bool,

};
