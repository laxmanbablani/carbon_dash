import React from 'react';
import { DismissibleTag as CarbonDismissibleTag } from '@carbon/react';

const DismissibleTag = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonDismissibleTag
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonDismissibleTag>
    );
};



export default DismissibleTag;
