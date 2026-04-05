import React from 'react';
import { Heading as CarbonHeading } from '@carbon/react';

const Heading = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonHeading
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonHeading>
    );
};



export default Heading;
