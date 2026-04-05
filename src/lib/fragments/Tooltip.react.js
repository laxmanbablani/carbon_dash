import React from 'react';
import { Tooltip as CarbonTooltip } from '@carbon/react';

const Tooltip = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        align,
        defaultOpen,
        description,
        ...otherProps
    } = props;
    return (
        <CarbonTooltip
            id={id}
            className={className}
            style={style}
            align={align}
            defaultOpen={defaultOpen}
            description={description}
            {...otherProps}
        >
            {children}
        </CarbonTooltip>
    );
};



export default Tooltip;
