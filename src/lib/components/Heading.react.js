import React from 'react';
import PropTypes from 'prop-types';
import { Heading as CarbonHeading } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const Heading = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;
    return (
        <CarbonHeading id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}>
            {children}
        </CarbonHeading>
    );
};

Heading.propTypes = {
    id: PropTypes.string,
    children: PropTypes.node,
    className: PropTypes.string,
    style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    level: PropTypes.oneOf([1,2,3,4,5,6]),
};

export default Heading;
