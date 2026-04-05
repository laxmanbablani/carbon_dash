import React from 'react';
import { OrderedList as CarbonOrderedList } from '@carbon/react';

const OrderedList = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonOrderedList
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonOrderedList>
    );
};



export default OrderedList;
