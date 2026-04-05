import React from 'react';
import { ContainedList as CarbonContainedList } from '@carbon/react';

const ContainedList = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonContainedList
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonContainedList>
    );
};



export default ContainedList;
