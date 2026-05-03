import React from 'react';
import PropTypes from 'prop-types';
import { Breadcrumb as CarbonBreadcrumb, BreadcrumbSkeleton as CarbonBreadcrumbSkeleton } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const Breadcrumb = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;
    if (loading_state && loading_state.is_loading) {
        return <CarbonBreadcrumbSkeleton id={id} className={className} />;
    }
    return <CarbonBreadcrumb id={id} className={className} style={style} data-dash-is-loading={getLoadingState(loading_state) || undefined} {...others}>{children}</CarbonBreadcrumb>;
};
Breadcrumb.propTypes = {
    id: PropTypes.string, children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    noTrailingSlash: PropTypes.bool, size: PropTypes.oneOf(['sm','md']), ariaLabel: PropTypes.string,
};
Breadcrumb.defaultProps = { noTrailingSlash: false, size: 'md' };
export default Breadcrumb;
