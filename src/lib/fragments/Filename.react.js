import React from 'react';
import { Filename as CarbonFilename } from '@carbon/react';

const Filename = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFilename
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFilename>
    );
};



export default Filename;
