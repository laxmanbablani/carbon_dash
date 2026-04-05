import React from 'react';
import { SlugContent as CarbonSlugContent } from '@carbon/react';

const SlugContent = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSlugContent
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSlugContent>
    );
};



export default SlugContent;
