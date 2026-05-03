import React from 'react';
import PropTypes from 'prop-types';
import { Row as CarbonRow } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * Row is a wrapper for the Carbon Row component.
 * Provides a grid row container for layout columns.
 */
const Row = (props) => {
    const {
        id,
        children,
        className = '',
        style = {},
        loading_state,
        as: asElement = 'div',
        condensed = false,
        narrow = false,
        ...others
    } = props;

    return (
        <CarbonRow
            id={id}
            className={className}
            style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            as={asElement}
            condensed={condensed}
            narrow={narrow}
            {...others}
        >
            {children}
        </CarbonRow>
    );
};

Row.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

    /** The content of the row */
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

    /** Provide a custom element type to render as the outermost element */
    as: PropTypes.oneOfType([PropTypes.string, PropTypes.elementType]),

    /** Collapse the gutter to 1px. Useful for fluid layouts */
    condensed: PropTypes.bool,

    /** Container hangs 16px into the gutter. Useful for typographic alignment */
    narrow: PropTypes.bool,
};

Row.defaultProps = {
    as: 'div',
    condensed: false,
    narrow: false,
};

export default Row;
