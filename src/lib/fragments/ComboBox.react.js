import React from 'react';
import { ComboBox as CarbonComboBox } from '@carbon/react';

const ComboBox = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonComboBox
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonComboBox>
    );
};



export default ComboBox;
