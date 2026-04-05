import React from 'react';
import { Row as CarbonRow } from '@carbon/react';

const Row = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        condensed,
        narrow,
        ...otherProps
    } = props;
    return (
        <CarbonRow
            id={id}
            className={className}
            style={style}
            condensed={condensed}
            narrow={narrow}
            {...otherProps}
        >
            {children}
        </CarbonRow>
    );
};



export default Row;
