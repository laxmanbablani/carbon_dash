import React from 'react';
import { Accordion as CarbonAccordion } from '@carbon/react';

const Accordion = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        align,
        isFlush,
        size,
        ...otherProps
    } = props;
    return (
        <CarbonAccordion
            id={id}
            className={className}
            style={style}
            align={align}
            isFlush={isFlush}
            size={size}
            {...otherProps}
        >
            {children}
        </CarbonAccordion>
    );
};



export default Accordion;
