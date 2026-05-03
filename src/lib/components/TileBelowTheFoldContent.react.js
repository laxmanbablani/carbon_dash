import React from 'react';
import PropTypes from 'prop-types';
import { TileBelowTheFoldContent as CarbonTileBelow } from '@carbon/react';

const TileBelowTheFoldContent = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;
    return (
        <CarbonTileBelow id={id} className={className} style={style}
            data-dash-is-loading={loading_state?.is_loading || undefined} {...others}>
            {children}
        </CarbonTileBelow>
    );
};
TileBelowTheFoldContent.propTypes = {
    id: PropTypes.string, children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
};
export default TileBelowTheFoldContent;
