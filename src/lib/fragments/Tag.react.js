import React from 'react';
import { Tag as CarbonTag } from '@carbon/react';

const Tag = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        type,
        size,
        disabled,
        ...otherProps
    } = props;
    return (
        <CarbonTag
            id={id}
            className={className}
            style={style}
            type={type}
            size={size}
            disabled={disabled}
            {...otherProps}
        >
            {children}
        </CarbonTag>
    );
};



export default Tag;
