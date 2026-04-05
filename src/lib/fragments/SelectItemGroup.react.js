import React from 'react';
import { SelectItemGroup as CarbonSelectItemGroup } from '@carbon/react';

const SelectItemGroup = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSelectItemGroup
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSelectItemGroup>
    );
};



export default SelectItemGroup;
