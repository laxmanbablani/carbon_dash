import React from 'react';
import { FlexGrid as CarbonFlexGrid } from '@carbon/react';

const FlexGrid = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFlexGrid
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFlexGrid>
    );
};



export default FlexGrid;
