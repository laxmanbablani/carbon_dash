import React from 'react';
import PropTypes from 'prop-types';
import { Column as CarbonColumn } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * Column is a wrapper for the Carbon Column component.
 * Provides responsive column spans for each breakpoint.
 */
const Column = (props) => {
    const {
        id,
        children,
        className = '',
        style = {},
        loading_state,
        as: asElement,
        sm,
        md,
        lg,
        xlg,
        max,
        ...others
    } = props;

    return (
        <CarbonColumn
            id={id}
            className={className}
            style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            as={asElement}
            sm={sm}
            md={md}
            lg={lg}
            xlg={xlg}
            max={max}
            {...others}
        >
            {children}
        </CarbonColumn>
    );
};

const spanPropType = PropTypes.oneOfType([
    PropTypes.bool,
    PropTypes.number,
    PropTypes.shape({
        span: PropTypes.oneOfType([PropTypes.number, PropTypes.string]),
        offset: PropTypes.number,
        start: PropTypes.number,
        end: PropTypes.number,
    }),
    PropTypes.oneOf(['25%', '50%', '75%', '100%']),
]);

Column.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

    /** The content of the column */
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

    /** Provide a custom element to render instead of the default div */
    as: PropTypes.oneOfType([PropTypes.string, PropTypes.elementType]),

    /** Specify column span for the sm breakpoint (up to 672px, 4 columns) */
    sm: spanPropType,

    /** Specify column span for the md breakpoint (up to 1056px, 8 columns) */
    md: spanPropType,

    /** Specify column span for the lg breakpoint (up to 1312px, 16 columns) */
    lg: spanPropType,

    /** Specify column span for the xlg breakpoint (up to 1584px, 16 columns) */
    xlg: spanPropType,

    /** Specify column span for the max breakpoint (16 columns) */
    max: spanPropType,
};

Column.defaultProps = {};

export default Column;
