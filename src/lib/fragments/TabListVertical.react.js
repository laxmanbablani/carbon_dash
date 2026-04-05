import React from 'react';
import { TabListVertical as CarbonTabListVertical } from '@carbon/react';

const TabListVertical = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTabListVertical
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTabListVertical>
    );
};



export default TabListVertical;
