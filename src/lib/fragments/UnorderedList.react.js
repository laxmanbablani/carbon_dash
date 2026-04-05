import React from 'react';
import { UnorderedList as CarbonUnorderedList } from '@carbon/react';

const UnorderedList = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonUnorderedList
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonUnorderedList>
    );
};



export default UnorderedList;
