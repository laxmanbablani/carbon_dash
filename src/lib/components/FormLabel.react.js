import React from 'react';
import PropTypes from 'prop-types';
import { FormLabel as CarbonFormLabel } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const FormLabel = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;
    return (
        <span
            id={id}
            className={className}
            style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
        >
            <CarbonFormLabel {...others}>
                {children}
            </CarbonFormLabel>
        </span>
    );
};

FormLabel.propTypes = {
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
};

FormLabel.defaultProps = {};

export default FormLabel;