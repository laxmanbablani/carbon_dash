import React from 'react';
import { CheckboxGroup as CarbonCheckboxGroup } from '@carbon/react';

const CheckboxGroup = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonCheckboxGroup
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonCheckboxGroup>
    );
};



export default CheckboxGroup;
