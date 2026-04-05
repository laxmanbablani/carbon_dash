import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Column is a wrapper for the Carbon Column component.
 */
export default class Column extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { sm } = this.props;
        const { md } = this.props;
        const { lg } = this.props;
        const { xlg } = this.props;
        const { max } = this.props;

        const RealComponent = LazyLoader['Column'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    sm={sm}
                    md={md}
                    lg={lg}
                    xlg={xlg}
                    max={max}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

Column.defaultProps = {
    className: '',
    sm: null,
    md: null,
    lg: null,
    xlg: null,
    max: null,
};

Column.propTypes = {
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
     * as
     */
    as_: PropTypes.any,

    /**
     * lg
     */
    lg: PropTypes.any,

    /**
     * max
     */
    max: PropTypes.any,

    /**
     * md
     */
    md: PropTypes.any,

    /**
     * sm
     */
    sm: PropTypes.any,

    /**
     * span
     */
    span: PropTypes.any,

    /**
     * xlg
     */
    xlg: PropTypes.any,

};
