import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Callout is a wrapper for the Carbon Callout component.
 */
export default class Callout extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['Callout'];
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

Callout.defaultProps = {
    className: '',
};

Callout.propTypes = {
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
     * actionButtonLabel
     */
    actionButtonLabel: PropTypes.any,

    /**
     * kind
     */
    kind: PropTypes.any,

    /**
     * lowContrast
     */
    lowContrast: PropTypes.any,

    /**
     * onActionButtonClick
     */
    onActionButtonClick: PropTypes.any,

    /**
     * statusIconDescription
     */
    statusIconDescription: PropTypes.any,

    /**
     * subtitle
     */
    subtitle: PropTypes.any,

    /**
     * title
     */
    title: PropTypes.any,

    /**
     * titleId
     */
    titleId: PropTypes.any,

};
