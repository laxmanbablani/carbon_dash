import React from 'react';
import { ButtonSkeleton as CarbonButtonSkeleton } from '@carbon/react';

const ButtonSkeleton = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonButtonSkeleton
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonButtonSkeleton>
    );
};



export default ButtonSkeleton;
