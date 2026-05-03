import React from 'react';
import PropTypes from 'prop-types';
import { BreadcrumbItem as CarbonBreadcrumbItem } from '@carbon/react';

const BreadcrumbItem = (props) => {
    const { id, children, className, style, loading_state, ...others } = props;
    return <CarbonBreadcrumbItem id={id} className={className} style={style} data-dash-is-loading={loading_state?.is_loading || undefined} {...others}>{children}</CarbonBreadcrumbItem>;
};
BreadcrumbItem.propTypes = {
    id: PropTypes.string, children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    href: PropTypes.string, isCurrentPage: PropTypes.bool, ariaLabel: PropTypes.string,
};
BreadcrumbItem.defaultProps = { isCurrentPage: false };
export default BreadcrumbItem;
