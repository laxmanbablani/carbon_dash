import React from 'react';
import PropTypes from 'prop-types';
import { HeaderName as CarbonHeaderName } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const HeaderName = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;
    return (
        <CarbonHeaderName
            id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonHeaderName>
    );
};

HeaderName.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * The content of the header name.
     */
    children: PropTypes.node,

    /**
     * Custom CSS class.
     */
    className: PropTypes.string,

    /**
     * Inline styles.
     */
    style: PropTypes.object,

    /**
     * Dash loading state.
     */
    loading_state: PropTypes.shape({
        is_loading: PropTypes.bool,
        prop_name: PropTypes.string,
        component_name: PropTypes.string,
    }),

    /**
     * Provide an href for the name to link to.
     */
    href: PropTypes.string,

    /**
     * Optionally specify a prefix to your header name.
     * Useful for companies, for example: IBM [Product Name] versus solely [Product Name].
     */
    prefix: PropTypes.string,

    /**
     * Provide a custom element or component to render the top-level node for the component.
     */
    as: PropTypes.elementType,

    /**
     * The base element to use to build the link. Defaults to `a`.
     * @deprecated Use `as` instead.
     */
    element: PropTypes.elementType,

    /**
     * Property to indicate if the side nav container is open (or not).
     */
    isSideNavExpanded: PropTypes.bool,
};

HeaderName.defaultProps = {
    prefix: 'IBM',
};

export default HeaderName;
