import React from 'react';
import { TabsSkeleton as CarbonTabsSkeleton } from '@carbon/react';

const TabsSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTabsSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTabsSkeleton>
    );
};



export default TabsSkeleton;
