import React from 'react';
import { ContainedListItem as CarbonContainedListItem } from '@carbon/react';

const ContainedListItem = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonContainedListItem
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonContainedListItem>
    );
};



export default ContainedListItem;
