import React from 'react';
import PropTypes from 'prop-types';
import { Layer as CarbonLayer } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * Layer provides a stacking context for Carbon components like Tooltips,
 * Modals, and Dropdowns. Nested layers maintain correct z-index ordering.
 */
const Layer = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;
    return (
        <CarbonLayer
            id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonLayer>
    );
};

Layer.propTypes = {
    id: PropTypes.string,
    children: PropTypes.node,
    className: PropTypes.string,
    style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    /** Level of nesting for layer context */
    level: PropTypes.number,
};

Layer.defaultProps = { level: 0 };

export default Layer;
