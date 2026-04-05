import React from 'react';
import { DefinitionTooltip as CarbonDefinitionTooltip } from '@carbon/react';

const DefinitionTooltip = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonDefinitionTooltip
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonDefinitionTooltip>
    );
};



export default DefinitionTooltip;
