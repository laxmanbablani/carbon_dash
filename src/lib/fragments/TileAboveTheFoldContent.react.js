import React from 'react';
import { TileAboveTheFoldContent as CarbonTileAboveTheFoldContent } from '@carbon/react';

const TileAboveTheFoldContent = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTileAboveTheFoldContent
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTileAboveTheFoldContent>
    );
};



export default TileAboveTheFoldContent;
