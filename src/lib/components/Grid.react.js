import React from 'react';
import PropTypes from 'prop-types';
import { Grid as CarbonGrid } from '@carbon/react';

/**
 * Grid is a wrapper for the Carbon Grid component.
 * Provides the top-level grid container for layout.
 */
const Grid = (props) => {
    const {
        id,
        children,
        className = '',
        style = {},
        loading_state,
        condensed = false,
        fullWidth = false,
        narrow = false,
        align,
        ...others
    } = props;

    return (
        <CarbonGrid
            id={id}
            className={className}
            style={style}
            data-dash-is-loading={loading_state?.is_loading || undefined}
            condensed={condensed}
            fullWidth={fullWidth}
            narrow={narrow}
            align={align}
            {...others}
        >
            {children}
        </CarbonGrid>
    );
};

Grid.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

    /** The content of the grid */
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

    /** Specify grid alignment: 'start', 'center', or 'end' */
    align: PropTypes.oneOf(['start', 'center', 'end']),

    /** Collapse the gutter to 1px. Useful for fluid layouts */
    condensed: PropTypes.bool,

    /** Remove the default max width the grid has set */
    fullWidth: PropTypes.bool,

    /** Container hangs 16px into the gutter. Useful for typographic alignment */
    narrow: PropTypes.bool,
};

Grid.defaultProps = {
    condensed: false,
    fullWidth: false,
    narrow: false,
};

export default Grid;
