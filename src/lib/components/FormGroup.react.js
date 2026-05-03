import React from 'react';
import PropTypes from 'prop-types';
import { FormGroup as CarbonFormGroup } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const FormGroup = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;
    return (
        <CarbonFormGroup
            id={id}
            className={className}
            style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonFormGroup>
    );
};

FormGroup.propTypes = {
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
    legendText: PropTypes.node.isRequired,
    legendId: PropTypes.node,
    message: PropTypes.bool,
    messageText: PropTypes.string,
    invalid: PropTypes.bool,
    disabled: PropTypes.bool,
};

FormGroup.defaultProps = {
    message: false,
    messageText: '',
    invalid: false,
    disabled: false,
};

export default FormGroup;