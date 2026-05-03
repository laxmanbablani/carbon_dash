import React from 'react';
import PropTypes from 'prop-types';
import { ProgressBar as CarbonProgressBar } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const ProgressBar = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;
    return <CarbonProgressBar id={id} className={className} style={style} data-dash-is-loading={getLoadingState(loading_state) || undefined} {...others}>{children}</CarbonProgressBar>;
};
ProgressBar.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func, children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    value: PropTypes.number, max: PropTypes.number, label: PropTypes.node, helperText: PropTypes.node,
    hideLabel: PropTypes.bool, size: PropTypes.oneOf(['big','small']),
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string), persistence_type: PropTypes.oneOf(['local','session','memory']),
};
ProgressBar.defaultProps = { value: 0, max: 100, size: 'big' };
export default ProgressBar;
