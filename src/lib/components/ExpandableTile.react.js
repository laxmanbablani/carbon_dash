import React from 'react';
import PropTypes from 'prop-types';
import { ExpandableTile as CarbonExpandableTile } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const ExpandableTile = (props) => {
    const { id, children, className = '', style = {}, loading_state, expanded = false, ...others } = props;

    const handleBeforeClick = () => {
        if (props.setProps) props.setProps({ expanded: !expanded });
    };

    return (
        <CarbonExpandableTile
            id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            expanded={expanded}
            onBeforeClick={handleBeforeClick}
            {...others}
        >
            {children}
        </CarbonExpandableTile>
    );
};

ExpandableTile.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func,
    children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    /** Whether the tile is expanded */
    expanded: PropTypes.bool,
    /** The tile's title (above fold) */
    tileText: PropTypes.node,
    /** Max height before expanding */
    tileMaxHeight: PropTypes.number,
    /** Whether to collapse on expand */
    tileCollapsedText: PropTypes.node,
    /** Whether this is the below-fold content */
    belowFold: PropTypes.bool,
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

ExpandableTile.defaultProps = { expanded: false };

export default ExpandableTile;
