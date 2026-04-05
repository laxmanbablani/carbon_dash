import React from 'react';
import { AccordionItem as CarbonAccordionItem } from '@carbon/react';

const AccordionItem = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        title,
        open,
        ...otherProps
    } = props;
    const onHeadingClick = (...args) => {
        if (setProps) {
            setProps({
                open: !props.open,
            });
        }
    };

    return (
        <CarbonAccordionItem
            id={id}
            className={className}
            style={style}
            title={title}
            open={open}
            onHeadingClick={onHeadingClick}
            {...otherProps}
        >
            {children}
        </CarbonAccordionItem>
    );
};



export default AccordionItem;
