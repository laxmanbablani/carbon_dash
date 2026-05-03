import React from 'react';
import PropTypes from 'prop-types';
import { SelectItem as CarbonSelectItem } from '@carbon/react';

const SelectItem = (props) => {
    const { id, children, className, style, loading_state, ...others } = props;
    return (
        <CarbonSelectItem
            id={id} className={className} style={style}
            data-dash-is-loading={loading_state?.is_loading || undefined}
            {...others}
        />
    );
};

SelectItem.propTypes = {
    id: PropTypes.string,
    children: PropTypes.node,
    className: PropTypes.string,
    style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    /** The value of the option */
    value: PropTypes.any.isRequired,
    /** The display text */
    text: PropTypes.string.isRequired,
    /** Whether the option is disabled */
    disabled: PropTypes.bool,
};

SelectItem.defaultProps = { disabled: false };

export default SelectItem;
