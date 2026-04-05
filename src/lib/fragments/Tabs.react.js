import React from 'react';
import { Tabs as CarbonTabs } from '@carbon/react';

const Tabs = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        selectedIndex,
        ...otherProps
    } = props;
    const onChange = (...args) => {
        if (setProps) {
            setProps({
                selectedIndex: args[0].selectedIndex,
            });
        }
    };

    return (
        <CarbonTabs
            id={id}
            className={className}
            style={style}
            selectedIndex={selectedIndex}
            onChange={onChange}
            {...otherProps}
        >
            {children}
        </CarbonTabs>
    );
};



export default Tabs;
