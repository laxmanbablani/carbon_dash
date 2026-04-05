import React from 'react';
import { SelectableTag as CarbonSelectableTag } from '@carbon/react';

const SelectableTag = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSelectableTag
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSelectableTag>
    );
};



export default SelectableTag;
