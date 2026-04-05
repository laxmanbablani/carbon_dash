import React from 'react';
import { ProgressStep as CarbonProgressStep } from '@carbon/react';

const ProgressStep = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        label,
        description,
        secondaryLabel,
        disabled,
        ...otherProps
    } = props;
    return (
        <CarbonProgressStep
            id={id}
            className={className}
            style={style}
            label={label}
            description={description}
            secondaryLabel={secondaryLabel}
            disabled={disabled}
            {...otherProps}
        >
            {children}
        </CarbonProgressStep>
    );
};



export default ProgressStep;
