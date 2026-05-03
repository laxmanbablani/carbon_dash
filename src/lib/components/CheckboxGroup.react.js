import React from 'react';
import PropTypes from 'prop-types';
import { CheckboxGroup as CarbonCheckboxGroup } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const CheckboxGroup = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;
    return <CarbonCheckboxGroup id={id} className={className} style={style} data-dash-is-loading={getLoadingState(loading_state) || undefined} {...others}>{children}</CarbonCheckboxGroup>;
};
CheckboxGroup.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func, children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    legendText: PropTypes.node, helperText: PropTypes.node, orientation: PropTypes.oneOf(['horizontal','vertical']),
    invalid: PropTypes.bool, invalidText: PropTypes.node, warn: PropTypes.bool, warnText: PropTypes.node, readOnly: PropTypes.bool,
};
CheckboxGroup.defaultProps = { orientation: 'horizontal', invalid: false, warn: false, readOnly: false };
export default CheckboxGroup;
