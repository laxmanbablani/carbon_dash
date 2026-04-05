import React from 'react';
import { TabPanel as CarbonTabPanel } from '@carbon/react';

const TabPanel = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTabPanel
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTabPanel>
    );
};



export default TabPanel;
