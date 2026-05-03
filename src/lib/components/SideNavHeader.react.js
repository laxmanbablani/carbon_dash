import React from 'react';
import PropTypes from 'prop-types';
import { SideNavHeader as CarbonComponent } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const SideNavHeader = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;
    return (
        <CarbonComponent
            id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonComponent>
    );
};

SideNavHeader.propTypes = {
    id: PropTypes.string,
    children: PropTypes.node,
    className: PropTypes.string,
    style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
};

export default SideNavHeader;
