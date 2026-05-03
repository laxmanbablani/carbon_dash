import React from 'react';
import PropTypes from 'prop-types';
import { InlineNotification as CarbonInlineNotification } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const InlineNotification = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;
    return <CarbonInlineNotification id={id} className={className} style={style} data-dash-is-loading={getLoadingState(loading_state) || undefined} {...others}>{children}</CarbonInlineNotification>;
};
InlineNotification.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func, children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    title: PropTypes.string, subtitle: PropTypes.node, kind: PropTypes.oneOf(['error','info','info-square','success','warning']),
    lowContrast: PropTypes.bool, hideCloseButton: PropTypes.bool, statusIconDescription: PropTypes.string,
    role: PropTypes.string, onCloseButtonClick: PropTypes.func,
};
InlineNotification.defaultProps = { kind: 'info', lowContrast: false, hideCloseButton: false };
export default InlineNotification;
