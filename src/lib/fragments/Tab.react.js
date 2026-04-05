import React from 'react';
import { Tab as CarbonTab } from '@carbon/react';

const Tab = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        label,
        disabled,
        ...otherProps
    } = props;
    return (
        <CarbonTab
            id={id}
            className={className}
            style={style}
            label={label}
            disabled={disabled}
            {...otherProps}
        >
            {children}
        </CarbonTab>
    );
};



export default Tab;
