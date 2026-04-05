import React from 'react';
import { FormItem as CarbonFormItem } from '@carbon/react';

const FormItem = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFormItem
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFormItem>
    );
};



export default FormItem;
