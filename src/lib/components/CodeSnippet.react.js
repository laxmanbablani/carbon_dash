import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * CodeSnippet is a wrapper for the Carbon CodeSnippet component.
 */
export default class CodeSnippet extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;

        const RealComponent = LazyLoader['CodeSnippet'];
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

CodeSnippet.defaultProps = {
    className: '',
};

CodeSnippet.propTypes = {
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
     * autoAlign
     */
    autoAlign: PropTypes.any,

    /**
     * ariaLabel
     */
    ariaLabel: PropTypes.any,

    /**
     * copyButtonDescription
     */
    copyButtonDescription: PropTypes.any,

    /**
     * copyText
     */
    copyText: PropTypes.any,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * feedback
     */
    feedback: PropTypes.any,

    /**
     * feedbackTimeout
     */
    feedbackTimeout: PropTypes.any,

    /**
     * hideCopyButton
     */
    hideCopyButton: PropTypes.any,

    /**
     * light
     */
    light: PropTypes.any,

    /**
     * maxCollapsedNumberOfRows
     */
    maxCollapsedNumberOfRows: PropTypes.any,

    /**
     * maxExpandedNumberOfRows
     */
    maxExpandedNumberOfRows: PropTypes.any,

    /**
     * minCollapsedNumberOfRows
     */
    minCollapsedNumberOfRows: PropTypes.any,

    /**
     * minExpandedNumberOfRows
     */
    minExpandedNumberOfRows: PropTypes.any,

    /**
     * onClick
     */
    onClick: PropTypes.any,

    /**
     * showLessText
     */
    showLessText: PropTypes.any,

    /**
     * showMoreText
     */
    showMoreText: PropTypes.any,

    /**
     * type
     */
    type: PropTypes.any,

    /**
     * wrapText
     */
    wrapText: PropTypes.any,

};
