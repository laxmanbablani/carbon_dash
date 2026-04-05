import React from 'react';
import { AccordionItem as CarbonAccordionItem } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const AccordionItem = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        title = 'Accordion Title',
        open = null,
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
            data-dash-is-loading={getLoadingState(loading_state)}
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
