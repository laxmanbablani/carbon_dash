import React from 'react';
import { Tile as CarbonTile } from '@carbon/react';

const Tile = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTile
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTile>
    );
};



export default Tile;
