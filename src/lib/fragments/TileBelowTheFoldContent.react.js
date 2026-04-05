import React from 'react';
import { TileBelowTheFoldContent as CarbonTileBelowTheFoldContent } from '@carbon/react';

const TileBelowTheFoldContent = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonTileBelowTheFoldContent
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonTileBelowTheFoldContent>
    );
};



export default TileBelowTheFoldContent;
