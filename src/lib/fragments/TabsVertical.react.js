import React from 'react';
import { TabsVertical as CarbonTabsVertical } from '@carbon/react';

const TabsVertical = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTabsVertical
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTabsVertical>
    );
};



export default TabsVertical;
