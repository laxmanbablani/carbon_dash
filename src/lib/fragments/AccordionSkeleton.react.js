import React from 'react';
import { AccordionSkeleton as CarbonAccordionSkeleton } from '@carbon/react';

const AccordionSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonAccordionSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonAccordionSkeleton>
    );
};



export default AccordionSkeleton;
