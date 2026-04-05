import React from 'react';
import { ListItem as CarbonListItem } from '@carbon/react';

const ListItem = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonListItem
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonListItem>
    );
};



export default ListItem;
