import React from 'react';
import { TabList as CarbonTabList } from '@carbon/react';

const TabList = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        contained,
        ...otherProps
    } = props;
    return (
        <CarbonTabList
            id={id}
            className={className}
            style={style}
            contained={contained}
            {...otherProps}
        >
            {children}
        </CarbonTabList>
    );
};



export default TabList;
