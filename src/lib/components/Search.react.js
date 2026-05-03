import React from 'react';
import PropTypes from 'prop-types';
import { Search as CarbonSearch, SearchSkeleton as CarbonSearchSkeleton } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const Search = (props) => {
    const { id, children, className = '', style = {}, loading_state, value, ...others } = props;

    if (loading_state && loading_state.is_loading) {
        return <CarbonSearchSkeleton id={id} className={className} />;
    }

    const handleChange = (e) => {
        if (props.setProps) props.setProps({ value: e.target?.value ?? e });
    };

    return (
        <CarbonSearch
            id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            value={value}
            onChange={handleChange}
            {...others}
        />
    );
};

Search.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func,
    children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    /** Current value of the search input */
    value: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
    /** Label text */
    labelText: PropTypes.node,
    /** Placeholder text */
    placeholder: PropTypes.string,
    /** Whether disabled */
    disabled: PropTypes.bool,
    /** Size */
    size: PropTypes.oneOf(['sm', 'md', 'lg']),
    /** Close button label */
    closeButtonLabelText: PropTypes.string,
    /** Whether expanded (small screens) */
    isExpanded: PropTypes.bool,
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

Search.defaultProps = { disabled: false, size: 'md', isExpanded: true };

export default Search;
