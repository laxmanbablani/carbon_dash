import React from 'react';
import PropTypes from 'prop-types';
import { ContentSwitcher as CarbonContentSwitcher } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const ContentSwitcher = (props) => {
    const {
        id,
        children,
        className = '',
        style = {},
        loading_state,
        selectedIndex = 0,
        selectionMode = 'automatic',
        size = 'md',
        lowContrast = false,
        ...others
    } = props;

    const handleChange = (params) => {
        if (props.setProps && params.index !== undefined) {
            props.setProps({ selected_index: params.index });
        }
    };

    return (
        <CarbonContentSwitcher
            id={id}
            className={className}
            style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            selectedIndex={selectedIndex}
            selectionMode={selectionMode}
            size={size}
            lowContrast={lowContrast}
            onChange={handleChange}
            {...others}
        >
            {children}
        </CarbonContentSwitcher>
    );
};

ContentSwitcher.propTypes = {
    id: PropTypes.string,
    setProps: PropTypes.func,
    children: PropTypes.node,
    className: PropTypes.string,
    style: PropTypes.object,
    loading_state: PropTypes.shape({
        is_loading: PropTypes.bool,
        prop_name: PropTypes.string,
        component_name: PropTypes.string,
    }),
    selected_index: PropTypes.number,
    selectedIndex: PropTypes.number,
    selectionMode: PropTypes.oneOf(['automatic', 'manual']),
    size: PropTypes.oneOf(['sm', 'md', 'lg']),
    lowContrast: PropTypes.bool,
};

ContentSwitcher.defaultProps = {
    selectedIndex: 0,
    selectionMode: 'automatic',
    size: 'md',
    lowContrast: false,
};

export default ContentSwitcher;