import React from 'react';
import PropTypes from 'prop-types';
import { AspectRatio as CarbonAspectRatio } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * AspectRatio is a wrapper for the Carbon AspectRatio component.
 * Maintains a specific width:height ratio for its content.
 */
const AspectRatio = (props) => {
    const { id, children, className = '', style = {}, loading_state, ratio = '1x1', ...others } = props;
    return (
        <div id={id} data-dash-is-loading={getLoadingState(loading_state) || undefined}>
            <CarbonAspectRatio
                className={className}
                style={style}
                ratio={ratio}
                {...others}
            >
                {children}
            </CarbonAspectRatio>
        </div>
    );
};

AspectRatio.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

    /** Dash callback to update props */
    setProps: PropTypes.func,

    /** The content of the aspect ratio container */
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

    /** Specify the aspect ratio (width:height) to maintain */
    ratio: PropTypes.oneOf(['1x1', '2x3', '3x2', '3x4', '4x3', '1x2', '2x1', '9x16', '16x9']),
};

AspectRatio.defaultProps = {
    ratio: '1x1',
};

export default AspectRatio;