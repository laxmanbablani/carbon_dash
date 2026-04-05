import React from 'react';
import { Column as CarbonColumn } from '@carbon/react';

const Column = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        sm,
        md,
        lg,
        xlg,
        max,
        ...otherProps
    } = props;
    return (
        <CarbonColumn
            id={id}
            className={className}
            style={style}
            sm={sm}
            md={md}
            lg={lg}
            xlg={xlg}
            max={max}
            {...otherProps}
        >
            {children}
        </CarbonColumn>
    );
};



export default Column;
