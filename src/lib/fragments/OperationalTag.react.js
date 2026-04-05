import React from 'react';
import { OperationalTag as CarbonOperationalTag } from '@carbon/react';

const OperationalTag = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonOperationalTag
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonOperationalTag>
    );
};



export default OperationalTag;
