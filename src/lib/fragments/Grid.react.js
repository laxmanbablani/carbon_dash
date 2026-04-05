import React from 'react';
import { Grid as CarbonGrid } from '@carbon/react';

const Grid = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        condensed,
        narrow,
        fullWidth,
        ...otherProps
    } = props;
    return (
        <CarbonGrid
            id={id}
            className={className}
            style={style}
            condensed={condensed}
            narrow={narrow}
            fullWidth={fullWidth}
            {...otherProps}
        >
            {children}
        </CarbonGrid>
    );
};



export default Grid;
