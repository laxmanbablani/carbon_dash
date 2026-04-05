import React from 'react';
import { Dropdown as CarbonDropdown } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const Dropdown = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        selectedItem = null,
        items = [],
        label = 'Dropdown',
        title = 'Dropdown Title',
        ...otherProps
    } = props;
    const onChange = (...args) => {
        if (setProps) {
            setProps({
                selectedItem: args[0].selectedItem,
            });
        }
    };

    return (
        <CarbonDropdown
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            selectedItem={selectedItem}
            items={items}
            label={label}
            titleText={title}
            onChange={onChange}
            {...otherProps}
        >
            {children}
        </CarbonDropdown>
    );
};

export default Dropdown;
