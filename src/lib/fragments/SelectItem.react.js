import React from 'react';
import { SelectItem as CarbonSelectItem } from '@carbon/react';

const SelectItem = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        value,
        text,
        ...otherProps
    } = props;
    return (
        <CarbonSelectItem
            id={id}
            className={className}
            style={style}
            value={value}
            text={text}
            {...otherProps}
        >
            {children}
        </CarbonSelectItem>
    );
};



export default SelectItem;
