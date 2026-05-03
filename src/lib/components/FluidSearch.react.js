import React from 'react';
import PropTypes from 'prop-types';
import { FluidSearch as CarbonFluidSearch, FluidSearchSkeleton as CarbonFluidSearchSkeleton } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * FluidSearch is a full-width Search component.
 */
const FluidSearch = (props) => {
    const {
        id,
        children,
        className = '',
        style = {},
        loading_state,
        labelText,
        placeholder,
        value,
        ...others
    } = props;

    if (loading_state && loading_state.is_loading) {
        return <CarbonFluidSearchSkeleton id={id} className={className} />;
    }

    const handleChange = (e) => {
        if (props.setProps) {
            const target = e && e.target;
            props.setProps({ value: target ? target.value : e });
        }
    };

    return (
        <CarbonFluidSearch
            id={id}
            className={className}
            style={style}
            labelText={labelText}
            placeholder={placeholder}
            value={value}
            onChange={handleChange}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonFluidSearch>
    );
};

FluidSearch.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

    /** Dash callback to update props */
    setProps: PropTypes.func,

    /** The content of the search */
    children: PropTypes.node,

    /** Custom CSS class */
    className: PropTypes.string,

    /** Inline styles */
    style: PropTypes.object,

    /** Dash loading state */
    loading_state: PropTypes.shape({
        is_loading: PropTypes.bool,
        prop_name: PropTypes.string,
        component_name: PropTypes.string,
    }),

    /** Provide the label text for the search */
    labelText: PropTypes.node,

    /** Provide the placeholder text for the search */
    placeholder: PropTypes.string,

    /** The value of the search input */
    value: PropTypes.string,

    /** Specify whether the search is disabled */
    disabled: PropTypes.bool,

    /** Specify whether the search is in an invalid state */
    invalid: PropTypes.bool,

    /** Specify whether the search is in a warning state */
    warn: PropTypes.bool,

    /** Specify the size of the search */
    size: PropTypes.oneOf(['sm', 'md', 'lg']),

    /** Persistence settings */
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),
    persisted_props: PropTypes.arrayOf(PropTypes.string),
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};

FluidSearch.defaultProps = {
    disabled: false,
    invalid: false,
    warn: false,
    size: 'md',
};

export default FluidSearch;