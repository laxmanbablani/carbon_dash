import React from 'react';
import PropTypes from 'prop-types';
import { Pagination as CarbonPagination } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const Pagination = (props) => {
    const { id, children, className = '', style = {}, loading_state, page, pageSize, totalItems, ...others } = props;
    const handleChange = (data) => { if (props.setProps) props.setProps({ page: data.page, pageSize: data.pageSize }); };
    return <CarbonPagination id={id} className={className} style={style} page={page} pageSize={pageSize} totalItems={totalItems} onChange={handleChange} data-dash-is-loading={getLoadingState(loading_state) || undefined} {...others}>{children}</CarbonPagination>;
};
Pagination.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func, children: PropTypes.node,
    className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    backwardText: PropTypes.string, forwardText: PropTypes.string, itemsPerPageText: PropTypes.string, pageNumberText: PropTypes.string,
    page: PropTypes.number, pageSize: PropTypes.number, pageSizes: PropTypes.arrayOf(PropTypes.number), totalItems: PropTypes.number,
    disabled: PropTypes.bool, isLastPage: PropTypes.bool, pageInputDisabled: PropTypes.bool, size: PropTypes.oneOf(['sm','md','lg']),
};
Pagination.defaultProps = { page: 1, pageSize: 10, totalItems: 0, disabled: false, pageSizes: [10, 20, 30, 40, 50], backwardText: 'Previous page', forwardText: 'Next page', pageInputDisabled: false, size: 'md' };
export default Pagination;
