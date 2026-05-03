import React from 'react';
import PropTypes from 'prop-types';
import { ClickableTile as CarbonClickableTile } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const ClickableTile = (props) => {
    const { id, children, className = '', style = {}, loading_state, clicked = false, ...others } = props;

    const handleClick = () => {
        if (props.setProps) props.setProps({ clicked: !clicked, n_clicks: (props.n_clicks || 0) + 1 });
    };

    return (
        <CarbonClickableTile
            id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            onClick={handleClick}
            {...others}
        >
            {children}
        </CarbonClickableTile>
    );
};

ClickableTile.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func,
    children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    /** Whether the tile has been clicked */
    clicked: PropTypes.bool,
    /** Click counter */
    n_clicks: PropTypes.number,
    /** Whether the tile is disabled */
    disabled: PropTypes.bool,
    /** href to render as a link */
    href: PropTypes.string,
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

ClickableTile.defaultProps = { clicked: false, disabled: false, n_clicks: 0 };

export default ClickableTile;
