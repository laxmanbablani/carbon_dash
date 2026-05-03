import React from 'react';
import PropTypes from 'prop-types';
import { Switch as CarbonSwitch } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const Switch = (props) => {
    const {
        id,
        children,
        className = '',
        style = {},
        loading_state,
        text,
        name,
        selected = false,
        disabled = false,
        index,
        ...others
    } = props;

    const handleClick = () => {
        if (props.setProps) {
            props.setProps({ selected: true, index: index });
        }
    };

    return (
        <CarbonSwitch
            id={id}
            className={className}
            style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            text={text}
            name={name}
            selected={selected}
            disabled={disabled}
            index={index}
            onClick={handleClick}
            {...others}
        >
            {children}
        </CarbonSwitch>
    );
};

Switch.propTypes = {
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
    text: PropTypes.string,
    name: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
    selected: PropTypes.bool,
    disabled: PropTypes.bool,
    index: PropTypes.number,
};

Switch.defaultProps = {
    selected: false,
    disabled: false,
};

export default Switch;