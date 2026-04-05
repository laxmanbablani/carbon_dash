import React from 'react';
import { Dropdown as CarbonDropdown } from '@carbon/react';

const Dropdown = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        selectedItem,
        items,
        label,
        title,
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
