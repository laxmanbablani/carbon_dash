import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * ProgressStep is a wrapper for the Carbon ProgressStep component.
 */
export default class ProgressStep extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { label } = this.props;
        const { description } = this.props;
        const { secondaryLabel } = this.props;
        const { disabled } = this.props;

        const RealComponent = LazyLoader['ProgressStep'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    label={label}
                    description={description}
                    secondaryLabel={secondaryLabel}
                    disabled={disabled}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

ProgressStep.defaultProps = {
    className: '',
    label: 'Step',
    description: 'Step description',
    secondaryLabel: '',
    disabled: false,
};

ProgressStep.propTypes = {
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
     * complete
     */
    complete: PropTypes.any,

    /**
     * current
     */
    current: PropTypes.any,

    /**
     * description
     */
    description: PropTypes.string,

    /**
     * disabled
     */
    disabled: PropTypes.bool,

    /**
     * index
     */
    index: PropTypes.any,

    /**
     * invalid
     */
    invalid: PropTypes.any,

    /**
     * label
     */
    label: PropTypes.node,

    /**
     * onClick
     */
    onClick: PropTypes.any,

    /**
     * overflowTooltipProps
     */
    overflowTooltipProps: PropTypes.any,

    /**
     * secondaryLabel
     */
    secondaryLabel: PropTypes.string,

    /**
     * tooltipId
     */
    tooltipId: PropTypes.any,

    /**
     * translateWithId
     */
    translateWithId: PropTypes.any,

};
