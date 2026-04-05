import React from 'react';
import { ButtonSet as CarbonButtonSet } from '@carbon/react';

const ButtonSet = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonButtonSet
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonButtonSet>
    );
};



export default ButtonSet;
