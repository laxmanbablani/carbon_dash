import React from 'react';
import PropTypes from 'prop-types';
import { Form as CarbonForm } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const Form = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;
    return (
        <CarbonForm
            id={id}
            className={className}
            style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonForm>
    );
};

Form.propTypes = {
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

Form.defaultProps = {};

export default Form;