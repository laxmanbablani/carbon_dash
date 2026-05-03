import React from 'react';
import PropTypes from 'prop-types';
import { TileAboveTheFoldContent as CarbonTileAbove } from '@carbon/react';

const TileAboveTheFoldContent = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;
    return (
        <CarbonTileAbove id={id} className={className} style={style}
            data-dash-is-loading={loading_state?.is_loading || undefined} {...others}>
            {children}
        </CarbonTileAbove>
    );
};
TileAboveTheFoldContent.propTypes = {
    id: PropTypes.string, children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
};
export default TileAboveTheFoldContent;
