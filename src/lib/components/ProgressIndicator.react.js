import React from 'react';
import PropTypes from 'prop-types';
import { ProgressIndicator as CarbonProgressIndicator, ProgressIndicatorSkeleton as CarbonSkeleton } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const ProgressIndicator = (props) => {
    const { id, children, className = '', style = {}, loading_state, currentIndex = 0, ...others } = props;
    if (loading_state && loading_state.is_loading) return <CarbonSkeleton id={id} className={className} />;
    return <CarbonProgressIndicator id={id} className={className} style={style} currentIndex={currentIndex} data-dash-is-loading={getLoadingState(loading_state) || undefined} {...others}>{children}</CarbonProgressIndicator>;
};
ProgressIndicator.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func, children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    currentIndex: PropTypes.number, vertical: PropTypes.bool, spaceEqually: PropTypes.bool,
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string), persistence_type: PropTypes.oneOf(['local','session','memory']),
};
ProgressIndicator.defaultProps = { currentIndex: 0, vertical: false, spaceEqually: false };
export default ProgressIndicator;
