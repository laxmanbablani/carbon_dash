import React from 'react';
import PropTypes from 'prop-types';
import { CodeSnippet as CarbonCodeSnippet } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * CodeSnippet is a wrapper for the Carbon CodeSnippet component.
 * Displays a block or inline snippet of code with copy functionality.
 */
const CodeSnippet = (props) => {
    const {
        id,
        children,
        className = '',
        style = {},
        loading_state,
        type = 'single',
        feedback,
        copyButtonDescription,
        wrapText = false,
        maxCollapsedNumberOfRows = 15,
        ...others
    } = props;

    return (
        <CarbonCodeSnippet
            id={id}
            className={className}
            style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            type={type}
            feedback={feedback}
            copyButtonDescription={copyButtonDescription}
            wrapText={wrapText}
            maxCollapsedNumberOfRows={maxCollapsedNumberOfRows}
            {...others}
        >
            {children}
        </CarbonCodeSnippet>
    );
};

CodeSnippet.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

    /** The code content to be displayed */
    children: PropTypes.node,

    /** Custom CSS class */
    className: PropTypes.string,

    /** Inline styles */
    style: PropTypes.object,

    /** Dash loading state */
    loading_state: PropTypes.shape({
        is_loading: PropTypes.bool,
        prop_name: PropTypes.string,
        component_name: PropTypes.string,
    }),

    /** The type of code snippet */
    type: PropTypes.oneOf(['single', 'multi', 'inline']),

    /** Specify the string displayed when the snippet is copied */
    feedback: PropTypes.string,

    /** Specify the description for the Copy Button */
    copyButtonDescription: PropTypes.string,

    /** Specify whether to wrap the text */
    wrapText: PropTypes.bool,

    /** Specify the maximum number of rows to show when collapsed */
    maxCollapsedNumberOfRows: PropTypes.number,

    /** Specify the time it takes for the feedback message to timeout */
    feedbackTimeout: PropTypes.number,

    /** Optional text to copy. If not specified, children innerText will be used */
    copyText: PropTypes.string,

    /** Specify whether or not a copy button should be rendered */
    hideCopyButton: PropTypes.bool,

    /** Specify whether or not the CodeSnippet should be disabled */
    disabled: PropTypes.bool,

    /** Specify the maximum number of rows to show when expanded */
    maxExpandedNumberOfRows: PropTypes.number,
};

CodeSnippet.defaultProps = {
    type: 'single',
    wrapText: false,
    maxCollapsedNumberOfRows: 15,
};

export default CodeSnippet;
