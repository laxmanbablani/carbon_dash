import React from 'react';
import { HeaderGlobalAction as CarbonHeaderGlobalAction } from '@carbon/react';

const HeaderGlobalAction = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonHeaderGlobalAction
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonHeaderGlobalAction>
    );
};



export default HeaderGlobalAction;
