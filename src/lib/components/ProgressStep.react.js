import React from 'react';
import PropTypes from 'prop-types';
import { ProgressStep as CarbonProgressStep } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const ProgressStep = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;
    return <CarbonProgressStep id={id} className={className} style={style} data-dash-is-loading={getLoadingState(loading_state) || undefined} {...others}>{children}</CarbonProgressStep>;
};
ProgressStep.propTypes = {
    id: PropTypes.string, children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    label: PropTypes.node, description: PropTypes.node, secondaryLabel: PropTypes.node,
    complete: PropTypes.bool, current: PropTypes.bool, invalid: PropTypes.bool, disabled: PropTypes.bool,
};
ProgressStep.defaultProps = { complete: false, current: false, invalid: false, disabled: false };
export default ProgressStep;
