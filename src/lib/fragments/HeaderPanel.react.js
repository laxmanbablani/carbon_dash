import React from 'react';
import { HeaderPanel as CarbonHeaderPanel } from '@carbon/react';

const HeaderPanel = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonHeaderPanel
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonHeaderPanel>
    );
};



export default HeaderPanel;
