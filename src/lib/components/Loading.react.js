import React from 'react';
import PropTypes from 'prop-types';
import { Loading as CarbonLoading } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * Loading is a wrapper for the Carbon Loading component.
 * Displays a loading indicator for async operations.
 */
const Loading = (props) => {
    const {
        id,
        className = '',
        style = {},
        loading_state,
        active = true,
        small = false,
        withOverlay = true,
        ...others
    } = props;

    return (
        <CarbonLoading
            id={id}
            className={className}
            style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            active={active}
            small={small}
            withOverlay={withOverlay}
            {...others}
        />
    );
};

Loading.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

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

    /** Specify whether the loading indicator should be spinning or not */
    active: PropTypes.bool,

    /** Specify whether you would like the small variant of Loading */
    small: PropTypes.bool,

    /** Specify whether you want the loader to be applied with an overlay */
    withOverlay: PropTypes.bool,

    /** Specify a description for the loading state */
    description: PropTypes.string,
};

Loading.defaultProps = {
    active: true,
    small: false,
    withOverlay: true,
    description: 'loading',
};

export default Loading;
