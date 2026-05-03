import React from 'react';
import PropTypes from 'prop-types';
import { FormItem as CarbonFormItem } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

/**
 * FormItem is a wrapper for the Carbon FormItem component.
 * Used to group form elements with their labels.
 */
const FormItem = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;
    return (
        <CarbonFormItem
            id={id}
            className={className}
            style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonFormItem>
    );
};

FormItem.propTypes = {
    /** The ID used to identify this component in Dash callbacks */
    id: PropTypes.string,

    /** Dash callback to update props */
    setProps: PropTypes.func,

    /** The content of the form item */
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
};

FormItem.defaultProps = {};

export default FormItem;