import React from 'react';
import { SlugActions as CarbonSlugActions } from '@carbon/react';

const SlugActions = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSlugActions
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSlugActions>
    );
};



export default SlugActions;
