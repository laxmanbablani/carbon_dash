import React from 'react';
import { TileGroup as CarbonTileGroup } from '@carbon/react';

const TileGroup = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTileGroup
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTileGroup>
    );
};



export default TileGroup;
