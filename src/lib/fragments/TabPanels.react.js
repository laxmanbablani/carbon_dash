import React from 'react';
import { TabPanels as CarbonTabPanels } from '@carbon/react';

const TabPanels = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTabPanels
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTabPanels>
    );
};



export default TabPanels;
