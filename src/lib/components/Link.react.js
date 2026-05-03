import React from 'react';
import PropTypes from 'prop-types';
import { Link as CarbonLink } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const Link = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;
    return (
        <CarbonLink
            id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonLink>
    );
};

Link.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func,
    children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    /** Provide the href for the link */
    href: PropTypes.string,
    /** Whether the link is inline (default) or standalone */
    inline: PropTypes.bool,
    /** Size of the link */
    size: PropTypes.oneOf(['sm', 'md', 'lg']),
    /** Whether to render the visited state */
    visited: PropTypes.bool,
    /** Whether the link is disabled */
    disabled: PropTypes.bool,
    /** Specify the target attribute */
    target: PropTypes.string,
};

Link.defaultProps = { inline: true, disabled: false };

export default Link;
