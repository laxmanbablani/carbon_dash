import React from 'react';
import { ProgressIndicator as CarbonProgressIndicator } from '@carbon/react';

const ProgressIndicator = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        currentIndex,
        vertical,
        spaceEqually,
        ...otherProps
    } = props;
    return (
        <CarbonProgressIndicator
            id={id}
            className={className}
            style={style}
            currentIndex={currentIndex}
            vertical={vertical}
            spaceEqually={spaceEqually}
            {...otherProps}
        >
            {children}
        </CarbonProgressIndicator>
    );
};



export default ProgressIndicator;
