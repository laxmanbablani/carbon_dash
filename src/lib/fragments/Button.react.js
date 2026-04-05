import React from 'react';
import { Button as CarbonButton } from '@carbon/react';

const Button = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        n_clicks,
        ...otherProps
    } = props;
    const onClick = (...args) => {
        if (setProps) {
            setProps({
                n_clicks: n_clicks + 1,
            });
        }
    };

    return (
        <CarbonButton
            id={id}
            className={className}
            style={style}
            n_clicks={n_clicks}
            onClick={onClick}
            {...otherProps}
        >
            {children}
        </CarbonButton>
    );
};



export default Button;
