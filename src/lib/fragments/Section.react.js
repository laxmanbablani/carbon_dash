import React from 'react';
import { Section as CarbonSection } from '@carbon/react';

const Section = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonSection
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonSection>
    );
};



export default Section;
