import React from 'react';
import { Loading as CarbonLoading } from '@carbon/react';

const Loading = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        active,
        withOverlay,
        small,
        ...otherProps
    } = props;
    return (
        <CarbonLoading
            id={id}
            className={className}
            style={style}
            active={active}
            withOverlay={withOverlay}
            small={small}
            {...otherProps}
        >
            {children}
        </CarbonLoading>
    );
};



export default Loading;
