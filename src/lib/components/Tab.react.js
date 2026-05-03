import React from 'react';
import PropTypes from 'prop-types';
import { Tab as CarbonTab } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const Tab = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;
    return (
        <CarbonTab
            id={id}
            className={className}
            style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonTab>
    );
};

Tab.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,
    /** The content of the tab */
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
    /** The label text for the tab */
    label: PropTypes.node,
    /** Whether the tab is disabled */
    disabled: PropTypes.bool,
    /** Whether the tab is selected. Overrides the parent's selectedIndex */
    selected: PropTypes.bool,
    /** Provide an href for the tab, making it an <a> element */
    href: PropTypes.string,
    /** Optional dismissible button label */
    closeButtonLabel: PropTypes.string,
    /** Whether the tab is dismissable */
    dismissable: PropTypes.bool,
};

Tab.defaultProps = {
    disabled: false,
};

export default Tab;
