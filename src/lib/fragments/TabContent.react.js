import React from 'react';
import { TabContent as CarbonTabContent } from '@carbon/react';

const TabContent = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTabContent
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTabContent>
    );
};



export default TabContent;
